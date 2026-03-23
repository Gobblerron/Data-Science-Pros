import time
import requests
import pandas as pd
from datetime import date, timedelta, datetime

# Configuration
EBIRD_API_KEY = "5vhjb11idsjt"
HEADERS = {"X-eBirdApiToken": EBIRD_API_KEY}

# Comparing North (Hamburg) vs. South (Munich)
REGIONS = {
    "Nord": {"code": "DE-HH", "lat": 53.55, "lon": 9.99},
    "Süd": {"code": "DE-BY", "lat": 48.13, "lon": 11.58}
}

bird_results = []
weather_results = []


# Step 1: Collect bird species richness via eBird API
def collect_bird_data(region_code, area_name, obs_date):
    y, m, d = obs_date.year, obs_date.month, obs_date.day
    url = (
        f"https://api.ebird.org/v2/data/obs/{region_code}/historic/{y}/{m}/{d}"
    )

    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        # Species richness = number of unique species codes observed on that day
        unique_species = {
            obs.get("speciesCode") for obs in data if "speciesCode" in obs
        }
        bird_results.append({
            "Date": obs_date.strftime("%Y-%m-%d"),
            "Region": area_name,
            "SpeciesRichness": len(unique_species)
        })
    else:
        print(f"Error eBird {area_name}: {response.status_code}")


# Step 2: Collect temperature data via Open-Meteo Archive API
def collect_weather_data(lat, lon, area_name, obs_date):
    date_str = obs_date.strftime("%Y-%m-%d")

    # AI assistance: looked up URL parameter structure for Open-Meteo Archive API
    url = (
        f"https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}&longitude={lon}"
        f"&start_date={date_str}&end_date={date_str}"
        f"&daily=temperature_2m_max&timezone=Europe%2FBerlin"
    )

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_max = data["daily"]["temperature_2m_max"][0]
        weather_results.append({
            "Date": date_str,
            "Region": area_name,
            "Max_Temp": temp_max
        })
    else:
        print(f"Error weather {area_name}: {response.status_code}")


# Data collection for March and April 2020 to 2025
print("Starting data collection (Spring 2020-2025)...")

for year in range(2020, 2026):
    current_date = date(year, 3, 1)
    end_date = date(year, 4, 30)

    while current_date <= end_date:
        for name, info in REGIONS.items():
            print(f"Date: {current_date} | Region: {name}")
            collect_bird_data(info["code"], name, current_date)
            collect_weather_data(info["lat"], info["lon"], name, current_date)
            time.sleep(0.1)  # AI assistance: reduced sleep to 0.1 to stay within rate limit
        current_date += timedelta(days=1)

# Save results as CSV files
df_birds = pd.DataFrame(bird_results)
df_birds.to_csv("bird_richness_spring.csv", index=False)

df_weather = pd.DataFrame(weather_results)
df_weather.to_csv("weather_temp_spring.csv", index=False)

# AI assistance: merge syntax for combined dataset
df_final = pd.merge(df_birds, df_weather, on=["Date", "Region"], how="left")
df_final.to_csv("final_richness_vs_temp.csv", index=False)

print("\nDone! All 3 files have been created.")