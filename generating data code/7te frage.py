import time
import requests
import pandas as pd
from datetime import datetime, timedelta

# API key and request header for eBird authentication
EBIRD_API_KEY = ""
HEADERS = {"": EBIRD_API_KEY}

# Time range for data collection
START_YEAR = 2020
END_YEAR = 2025

# Two regions for North vs. South comparison in Germany
REGIONS = {
    "Nord": {"code": "DE-HH", "lat": 53.55, "lon": 9.99},
    "Süd": {"code": "DE-BY", "lat": 48.13, "lon": 11.58}
}

# Duck species of interest with their eBird species codes
DUCK_SPECIES = {
    "mallar3": "Mallard",
    "gadwal1": "Gadwall",
    "eurwig": "Eurasian Wigeon",
    "tufduc": "Tufted Duck",
    "compocha": "Common Pochard"
}

# Lists to store collected records before converting to DataFrames
weather_records = []
bird_records = []

# Set up date range for the full collection period
current_date = datetime(START_YEAR, 1, 1)
end_date = datetime(END_YEAR, 12, 31)

print(f"Starting data collection via Open-Meteo: {START_YEAR} - {END_YEAR}")

while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")

    for area, info in REGIONS.items():

        # Step 1: Fetch daily max wind speed from Open-Meteo (no API key required)
        # AI assistance: looked up URL parameter structure for Open-Meteo Archive API
        w_url = (
            f"https://archive-api.open-meteo.com/v1/archive"
            f"?latitude={info['lat']}&longitude={info['lon']}"
            f"&start_date={date_str}&end_date={date_str}"
            f"&daily=wind_speed_10m_max&timezone=Europe%2FBerlin"
        )

        w_res = requests.get(w_url)
        w_json = w_res.json()

        # Extract wind value from response, default to 0 if missing
        if "daily" in w_json:
            wind = w_json["daily"]["wind_speed_10m_max"][0]
        else:
            wind = 0

        # Store weather record for this date and region
        weather_records.append({
            "date": date_str,
            "region": area,
            "wind_speed": wind
        })

        # Step 2: Fetch historic bird observation data from eBird
        y, m, d = current_date.year, current_date.month, current_date.day
        e_url = (
            f"https://api.ebird.org/v2/data/obs/{info['code']}/historic/{y}/{m}/{d}"
        )

        e_res = requests.get(e_url, headers=HEADERS)
        obs = e_res.json()

        # Filter observations to only include the duck species we are interested in
        if isinstance(obs, list):
            for s_code, s_name in DUCK_SPECIES.items():
                matches = [b for b in obs if b.get("speciesCode") == s_code]
                if matches:
                    bird_records.append({
                        "date": date_str,
                        "region": area,
                        "species": s_name,
                        "obs_freq": len(matches),
                        "count": sum(
                            int(b.get("howMany", 1)) for b in matches
                        )
                    })

        print(f"Done: {date_str} {area} | Wind: {wind} km/h")
        time.sleep(0.1)  # AI assistance: reduced sleep to 0.1 to stay within rate limit

    current_date += timedelta(days=1)

# Convert lists to DataFrames and save as CSV files 
df_w = pd.DataFrame(weather_records)
df_b = pd.DataFrame(bird_records)
#AI assistance: to find the to_csv function
df_w.to_csv("wetter_wind_daten.csv", index=False)
df_b.to_csv("enten_beobachtungen.csv", index=False)

# AI assistance: merge syntax for combined dataset
df_final = pd.merge(df_b, df_w, on=["date", "region"], how="left")
df_final.to_csv("analyse_wind_enten_deutschland.csv", index=False)

print("\nSuccess! All 3 files have been created.")
