import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
import numpy as np


st.set_page_config(page_title="Bird observations", layout = "wide")

#Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "main menu",
        options = ["Homepage", "Data and sources", "Research Question 1", "Research Question 2", "Research Question 3", "Research Question 4", "Research Question 5", "Research Question 6", "Research Question 7", "Research Question 8", "Research Question 9"],
        icons = ["house", "database", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill"],
        menu_icon ="cast",
        styles={
            "container": {"padding": "5!important", "background-color": "#0e1117"},
            "icon": {"color": "red", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#1d222c"},
            "nav-link-selected": {"background-color": "#000000"},
        }
    )
#--------------------------
#        HOMEPAGE
#--------------------------
if selected == "Homepage":
    st.title("Dashboard")
    st.title("Research Topic: Bird observations and its influences")
    st.image("Streamlit/Cranes_Homepage.png", width=2100)
    st.markdown("This image was generated with Google Gemini")
    
    st.subheader("Research Questions:")
    st.write("""
**1.** How does air Pollution affect bird observation frequency in Hamburg in the years 2021-2025 and which pollutant affects the birds the most?

**2.** How are hotspots of house sparrows in Berlin influenced by increased pollution in the years 2023-2025?

**3.** How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?

**4.** How does O3 concentration influence the observation frequency of feral pigeons in Berlin in the years 2021-2024?          
             
**5.** Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?

**6.** How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany?          
             
**7.** How does wind speed affect the observation frequency of duck species?
             
**8.** How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2024?

**9.** Did Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?
             """)

    st.info("💡**Use the main menu on the left to explore the contents of the Website.**")


    code = '''
                                                                                                                        ⠀⠀⠀⣀⣤⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
                                                                                                                    ⠀⠀⠀⠀⢀⣾⠛⠁⢰⣧⡈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⢸⣇⣼⡀⠻⠟⠁⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⢀⡞⣹⠙⣧⡀⠀⠀⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⣀⡴⠋⠀⣀⣴⣿⡷⠴⠞⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⢾⣁⣀⡤⠾⠛⠁⣸⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                            ⢠⡟⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⣠⣿⠁⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⢿⣶⠶⠿⠟⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠈⠙⠛⠿⠶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣀⣠⣤⣤⣤⣤⣤⣀⠀⠉⠙⠳⢦⣄⡀⣀⣤⣀⣀⡄⠀
                                                                                                                    ⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠈⠉⠻⢶⣀⠀⠀⠈⠉⢁⠈⠏⣿⣁⠀
                                                                                                                    ⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣀⣀⡴⠁⠀⠀⢙⣿⡾
                                                                                                                    ⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⣀⣠⡾⠟⠃
                                                                                                                    ⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡔⢊⣵⠞⠋⠁⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠉⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠈⠙⠳⠶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣴⠊⣁⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⡷⢶⡶⠶⠤⠔⢺⠃⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⢰⡇⠀⡇⠀⠀⠀⢸⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣤⣭⠿⠟⣃⣾⠋⠀⠀⢠⡟⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠉⠙⠛⢋⣿⣙⣶⣾⡿⢷⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠻⠧⠶⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        '''

    st.code(code, language=None)
    
    if st.button("🦆Duck button"):
        st.audio("Streamlit/quack_short.mp3", format="audio/mp3", autoplay=True)

    st.divider()

    st.markdown("""
<div style="font-size: 0.85rem; line-height: 1.4; color: #555;">
    <strong style="font-size: 1rem;">Imprint</strong><br>
    <strong>Project Group:</strong><br>
    Futun Gerisha – stu246828@mail.uni-kiel.de<br>
    Pia Stohn – stu224237@mail.uni-kiel.de<br>
    Dennis Frank – stu244762@mail.uni-kiel.de<br>
    Lisa Piontkowski – stu246963@mail.uni-kiel.de<br><br>
    <strong>Institution:</strong><br>
    Christian-Albrechts-Universität zu Kiel<br>
    Christian-Albrechts-Platz 4<br>
    24118 Kiel, Germany<br><br>
    <em>This website was created as part of a student research project.</em>
</div>
""", unsafe_allow_html=True)

#--------------------------
#      Data and sources
#--------------------------

if selected == "Data and sources":
    st.title("Data and Sources")
    st.subheader("Data description")

    st.write("""
             For our analysis, we integrated bird observation data with weather and environmental records. 
Our datasets were constructed by merging information from three different APIs into a 
time-series format.

**1. Data Sources (APIs)**

- **eBird API (Cornell Lab of Ornithology):** This was our primary source for bird observation
frequencies and species richness. We used the historical observation endpoints to
track species such as the Common Crane, Mallard and Rock Pigeons across specific European regions.

- **OpenWeather Air Pollution API:** This API was used to retrieve atmospheric data.
We specifically extracted concentrations of PM10, PM2.5 and O3 (Ozone) to correlate
bird activity with regional air quality.

- **Visual Crossing Weather API:** This API provided the meteorological context for our research
and supplied variables such as temperature and wind speed for the exact coordinates of 
our bird observations.


**2. Data Processing and Storage**

The raw data from these JSON-based APIs was cleaned, merged by date and region and
transformed into CSV files.

**Our main steps included:**
* **Merging:** Syncing bird observations with the nearest hourly weather and pollution records.
* **Data Normalization:** Handling missing or incorrect values and ensuring consistent units across all datasets.
* **Categorization:** Adding fields such as "Migration Windows" and "Arrival Day" to allow the comparative analysis shown in our visualizations.
             """)
    
    st.subheader("Data used:")

   
    with st.expander("Data for Research Question 1 (Hamburg Bird Counts)"):
        RQ_1 = pd.read_csv("Streamlit/RQ_1/hamburg_birdCounts_pollution_2021-2025.csv")
        st.dataframe(RQ_1, use_container_width=True)

    with st.expander("Data for Research Question 2 (Berlin Sparrows)"):
        RQ_2 = pd.read_csv("Streamlit/RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv")
        st.dataframe(RQ_2, use_container_width=True)

    with st.expander("Data for Research Question 3 (Species Richness SH)"):
        RQ_3 = pd.read_csv("Streamlit/RQ_3/rq_3_richness_sh_data.csv")
        st.dataframe(RQ_3, use_container_width=True)

    with st.expander("Data for Research Question 4 (Berlin Pigeons)"):
        RQ_4 = pd.read_csv("Streamlit/RQ_4/berlin_pigeon_pullution_2020_2024.csv")
        st.dataframe(RQ_4, use_container_width=True)

    with st.expander("Data for Research Question 5 (Europe Ducks)"):
        RQ_5 = pd.read_csv("Streamlit/RQ_5/europe_ducks_march_2020_2024.csv")
        RQ_5_2 = pd.read_csv("Streamlit/RQ_5/europe_ducks_recent_daily.csv")
        st.write("Historic Data:")
        st.dataframe(RQ_5, use_container_width=True)
        st.write("Recent Daily Data:")
        st.dataframe(RQ_5_2, use_container_width=True)

    with st.expander("Data for Research Question 6 (Richness vs. Temp)"):
        RQ_6 = pd.read_csv("Streamlit/RQ_6/final_richness_vs_temp.csv")
        st.dataframe(RQ_6, use_container_width=True)

    with st.expander("Data for Research Question 7 (Wind Analysis)"):
        RQ_7 = pd.read_csv("Streamlit/RQ_7/analyse_wind_enten_deutschland.csv")
        st.dataframe(RQ_7, use_container_width=True)

    with st.expander("Data for Research Question 8 (Migratory Observations SH)"):
        RQ_8 = pd.read_csv("Streamlit/RQ_8/migratory_observations_SH_2021-2025.csv")
        st.dataframe(RQ_8, use_container_width=True)

    with st.expander("Data for Research Question 9 (Crane Arrival)"):
        RQ_9 = pd.read_csv("Streamlit/RQ_9/craneArrival_pollution_updated.csv")
        st.dataframe(RQ_9, use_container_width=True)

#--------------------------
#    Research Questions
#--------------------------

if selected == "Research Question 1":
    st.title("Research Question 1")
    st.subheader("🏭How does air Pollution affect bird observation frequency in Hamburg in the years 2021-2025 and which pollutant affects the birds the most?")

    file_path_rq1 = "Streamlit/RQ_1/hamburg_birdCounts_pollution_2021-2025.csv"

    try:
        df_hamburg = pd.read_csv(file_path_rq1)
        df_hamburg["Date"] = pd.to_datetime(df_hamburg["Date"])

        pollutant_choice = st.selectbox(
            "Select pollutant to analyze:",
            ["PM2.5", "PM10"],
            key="rq1_pollutant_filter"
        )
        
        pollutant = f"{pollutant_choice}_mean"
        threshold = 25 if pollutant_choice == "PM2.5" else 50
        n_bins = 8

        plot_df = df_hamburg[[pollutant, "Total_Amount"]].dropna()
        plot_df = plot_df[plot_df[pollutant] >= 0]

        bin_edges = np.linspace(
            plot_df[pollutant].min(),
            plot_df[pollutant].max(),
            n_bins + 1
        )
        
        plot_df["pollution_bin"] = pd.cut(
            plot_df[pollutant],
            bins=bin_edges,
            include_lowest=True
        )

        summary = (
            plot_df.groupby("pollution_bin", observed=True)
            .agg(
                avg_birds=("Total_Amount", "mean"),
                median_birds=("Total_Amount", "median"),
                days=("Total_Amount", "size"),
                avg_pollution=(pollutant, "mean"),
            )
            .reset_index()
        )

        bin_left = np.array([interval.left for interval in summary["pollution_bin"]])
        bin_right = np.array([interval.right for interval in summary["pollution_bin"]])
        bin_mid = (bin_left + bin_right) / 2
        bin_width = bin_right - bin_left

        colors = np.where(bin_mid >= threshold, "firebrick", "royalblue")
        bin_labels = pd.Series(bin_left).round(1).astype(str) + "-" + pd.Series(bin_right).round(1).astype(str)

        fig1 = px.bar(
            summary,
            x=bin_mid,
            y="avg_birds",
            text=summary["avg_birds"].round(1).astype(str) + "<br>(" + summary["days"].astype(str) + " days)",
            title=f"Average Bird Observations vs. {pollutant_choice} Levels",
            labels={"avg_birds": "Average bird observations"},
            template="plotly_dark"
        )

        fig1.update_traces(
            marker_color=colors,
            width=bin_width * 0.9,
            textposition="outside",
            hovertemplate=(
                "<b>%{customdata[0]} µg/m³</b><br>"
                "Avg. Birds: %{customdata[1]}<br>"
                "Days in sample: %{customdata[3]}<extra></extra>"
            ),
            customdata=np.column_stack([
                bin_labels,
                summary["avg_birds"].round(1),
                summary["median_birds"].round(1),
                summary["days"],
                summary["avg_pollution"].round(2)
            ])
        )

        fig1.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='lines',
            line=dict(color='white', width=2, dash='dash'),
            name=f'Critical Threshold ({threshold} µg/m³)',
            showlegend=True
        ))

        fig1.add_vline(
            x=threshold,
            line_dash="dash",
            line_width=2,
            line_color="white"
        )

        fig1.update_layout(
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            xaxis=dict(
                tickmode="array",
                tickvals=bin_mid,
                ticktext=bin_labels,
                title=f"{pollutant_choice} Concentration Interval (µg/m³)"
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=600
        )

        st.plotly_chart(fig1, use_container_width=True)

        st.success("""
                This graph illustrates bird observations in Hamburg in relation to two major air pollutants: 
                PM10 and PM2.5. A critical threshold is displayed for each pollutant to evaluate potential 
                impacts on bird activity.

                **Key Observations:**
                * **PM2.5:** Interestingly, bird observations do not drop when the PM2.5 threshold is exceeded. 
                Instead, counts actually rise to an average of 246 individuals within the 
                36.6-45.6 µg/m³ range. This suggests that higher PM2.5 levels do not show a negative 
                correlation in this dataset.

                * **PM10:** In contrast, PM10 shows a different pattern. We observe a peak in numbers 
                at 38.2-47.5 µg/m³, before the threshold. The highest observation count 
                occurs exactly at the 47.5-56.8 µg/m³ interval. However, unlike PM2.5, 
                bird counts drop significantly once the concentration moves further beyond its threshold.

                **Conclusion:**
                The data indicates that bird observations remain relatively stable or even increase 
                during moderate pollution levels. They only appear to suffer once concentrations reach 
                very high values, like 63.6-72.6 µg/m³. 

                **Regarding which pollutant has a greater impact:** Although the PM2.5 threshold is lower, 
                it does not seem to affect observation numbers in this dataset. 
                However, PM10 shows a much clearer impact, as numbers drop quickly after its 
                specific threshold is reached. Therefore, based on this data, 
                **PM10 appears to influence bird observation frequency more significantly than PM2.5.**
                """)

        st.info(f"💡 **Critical Threshold:** The dashed white line represents the scientifically recommended air quality limit ({threshold} µg/m³ for {pollutant_choice})")

        if pollutant_choice == "PM2.5":
            st.info("💡 **PM2.5** consists of fine inhalable particles with diameters of 2.5 micrometers and smaller. These tiny particles mainly originate from combustion processes (e.g. vehicle engines, wood burning). Because of their size, they can penetrate deep into the lungs and even enter the bloodstream, posing a higher health risk to wildlife and humans.")
        else:
            st.info("💡 **PM10** refers to coarse inhalable particles with diameters generally 10 micrometers and smaller. These are often produced by mechanical processes like road dust resuspension, construction work, and industrial activities. They can irritate the eyes and upper respiratory tract.")

    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 2":
    st.title("Research Question 2")
    st.subheader("🐦How are hotspots of house sparrows in Berlin influenced by increased pollution in the years 2023-2025?")

    file_path_rq2 = "Streamlit/RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv"

    try:
        df_sparrows = pd.read_csv(file_path_rq2)
        df_sparrows["date"] = pd.to_datetime(df_sparrows["date"])
        df_sparrows = df_sparrows.sort_values("date")
        
        df_sparrows["diff_howMany"] = df_sparrows["sum_howMany_birds"].diff()
        df_sparrows["diff_pm2_5_mean"] = df_sparrows["pm2_5_mean"].diff()
        df_sparrows["diff_no2_mean"] = df_sparrows["no2_mean"].diff()
        
        df_sparrows = df_sparrows.dropna(subset=["diff_howMany", "diff_pm2_5_mean", "diff_no2_mean"])

        pm25_threshold = df_sparrows["diff_pm2_5_mean"].abs().quantile(0.95)
        no2_threshold = df_sparrows["diff_no2_mean"].abs().quantile(0.95)

        df_filtered = df_sparrows[
            (df_sparrows["diff_pm2_5_mean"].abs() >= pm25_threshold) |
            (df_sparrows["diff_no2_mean"].abs() >= no2_threshold)
        ].copy()

        birds_max = df_filtered["diff_howMany"].abs().max()
        pollution_max = max(
            df_filtered["diff_pm2_5_mean"].abs().max(),
            df_filtered["diff_no2_mean"].abs().max()
        )
        birds_limit = birds_max * 1.1
        pollution_limit = pollution_max * 1.1

        fig2 = go.Figure()

        fig2.add_trace(go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["diff_howMany"],
            mode="markers",
            name="Δ House Sparrows",
            showlegend=True,
            marker=dict(size=8, color="royalblue"),
            hovertemplate="<b>Δ House Sparrows</b><br>Date: %{x|%Y-%m-%d}<br>Change: %{y}<extra></extra>"
        ))

        fig2.add_trace(go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["diff_pm2_5_mean"],
            mode="markers",
            name="Δ PM2.5",
            yaxis="y2",
            showlegend=True,
            marker=dict(size=8, color="firebrick", opacity=0.8),
            hovertemplate="<b>Δ PM2.5</b><br>Date: %{x|%Y-%m-%d}<br>Change: %{y:.2f}<extra></extra>"
        ))

        fig2.add_trace(go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["diff_no2_mean"],
            mode="markers",
            name="Δ NO2",
            yaxis="y2",
            showlegend=True,
            marker=dict(size=8, color="#F1C40F", opacity=0.8),
            hovertemplate="<b>Δ NO2</b><br>Date: %{x|%Y-%m-%d}<br>Change: %{y:.2f}<extra></extra>"
        ))

        fig2.update_layout(
            title="Days with Strong Pollution Changes: Berlin (2023–2025)",
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            xaxis=dict(title="Date", showgrid=True, gridcolor="rgba(255,255,255,0.1)"),
            yaxis=dict(
                title="Change in House Sparrow Count",
                range=[-birds_limit, birds_limit],
                gridcolor="rgba(255,255,255,0.1)",
                zeroline=True,
                zerolinecolor="white"
            ),
            yaxis2=dict(
                title="Change in Pollution (PM2.5 / NO2)",
                overlaying="y",
                side="right",
                range=[pollution_limit, -pollution_limit],
                showgrid=False,
                zeroline=False
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            ),
            height=600,
            updatemenus=[
                dict(
                    type="dropdown",
                    direction="down",
                    x=1.0,
                    y=1.15,
                    showactive=True,
                    buttons=[
                        dict(label="Show all", method="update", args=[{"visible": [True, True, True]}]),
                        dict(label="Birds only", method="update", args=[{"visible": [True, False, False]}]),
                        dict(label="PM2.5 + Birds", method="update", args=[{"visible": [True, True, False]}]),
                        dict(label="NO2 + Birds", method="update", args=[{"visible": [True, False, True]}])
                    ]
                )
            ]
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.success("""
                    This graph illustrates the relationship between daily fluctuations in house sparrow counts 
                    at hotspots and changes in air pollutants (PM2.5 and NO2). By focusing on days with 
                    significant pollution volatility, we can evaluate the immediate behavioral responses 
                    of these bird populations.

                    **Key observations:** Significant changes in pollution and bird counts primarily cluster 
                    around the winter months, specifically from September to March. This seasonality likely 
                    correlates with increased heating activity. Interestingly, the response of house sparrows 
                    varies across the analyzed years. While some sharp declines in bird counts coincide 
                    with pollution spikes, we also observe positive spikes during similar conditions. 
                    For instance, a peak increase of 1,000 birds occurred when the NO2 value shifted by 16.11 µg/m³.

                    **Another example:** The data shows that pollution is not the only factor. The most 
                    significant drop in sparrow sightings (-2,250) was recorded on 2025-02-14, even though 
                    the NO2 concentration only decreased by 4.64 µg/m³ on that day. 

                    PM2.5 shows a similar inconsistent pattern.
                    """)

        st.divider()
        st.subheader("📊 Average House Sparrow Counts by Pollution Levels")

        bar_pollutant_choice = st.selectbox(
            "Select pollutant:",
            ["PM2.5", "NO2"],
            key="rq2_bar_pollutant_filter"
        )
        
        if bar_pollutant_choice == "PM2.5":
            bar_pollutant = "pm2_5_mean"
            bar_threshold = 25 
        else:
            bar_pollutant = "no2_mean"
            bar_threshold = 40 

        df_bar = df_sparrows[[bar_pollutant, "sum_howMany_birds"]].dropna()
        df_bar = df_bar[df_bar[bar_pollutant] >= 0]

        n_bins_berlin = 8
        bin_edges_berlin = np.linspace(
            df_bar[bar_pollutant].min(),
            df_bar[bar_pollutant].max(),
            n_bins_berlin + 1
        )
        
        df_bar["pollution_bin"] = pd.cut(
            df_bar[bar_pollutant],
            bins=bin_edges_berlin,
            include_lowest=True
        )

        summary_berlin = (
            df_bar.groupby("pollution_bin", observed=True)
            .agg(
                avg_birds=("sum_howMany_birds", "mean"),
                days=("sum_howMany_birds", "size")
            )
            .reset_index()
        )

        bin_l = np.array([i.left for i in summary_berlin["pollution_bin"]])
        bin_r = np.array([i.right for i in summary_berlin["pollution_bin"]])
        bin_m = (bin_l + bin_r) / 2
        bin_w = bin_r - bin_l
        bin_labs = pd.Series(bin_l).round(1).astype(str) + "–" + pd.Series(bin_r).round(1).astype(str)

        bar_colors = np.where(bin_m >= bar_threshold, "firebrick", "royalblue")

        fig_bar_berlin = go.Figure()

        fig_bar_berlin.add_trace(go.Bar(
            x=bin_m,
            y=summary_berlin["avg_birds"],
            text=summary_berlin["avg_birds"].round(1),
            marker_color=bar_colors,
            width=bin_w * 0.9,
            textposition="outside",
            name="Avg. House Sparrows",
            showlegend=False,
            customdata=bin_labs,
            hovertemplate="<b>%{customdata} µg/m³</b><br>Avg. Birds: %{y:.1f}<extra></extra>"
        ))

        fig_bar_berlin.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='lines',
            line=dict(color='white', width=2, dash='dash'),
            name=f'Critical Threshold ({bar_threshold} µg/m³)',
            showlegend=True
        ))

        fig_bar_berlin.add_vline(
            x=bar_threshold,
            line_dash="dash",
            line_width=2,
            line_color="white"
        )

        fig_bar_berlin.update_layout(
            title=f"Average House Sparrow counts vs. {bar_pollutant_choice} Levels (Berlin)",
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            xaxis=dict(
                tickmode="array",
                tickvals=bin_m,
                ticktext=bin_labs,
                title=f"{bar_pollutant_choice} Concentration (µg/m³)"
            ),
            yaxis_title="Average Sparrow Count",
            height=500,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig_bar_berlin, use_container_width=True)

        st.success("""
                   The bar chart shows the average house sparrow counts compared with PM2.5 and NO2 concentrations, along 
                    with their respective critical thresholds.

                    **Key observations:** The sparrow hotspots appear to be susceptible to PM2.5, as evidenced by the mostly 
                    steady decline in average sparrow counts once the threshold is reached. The NO2 values, however, paint a 
                    different picture: while counts drop around the threshold, they surprisingly begin to rise again as NO2 levels 
                    continue to increase.
                   
                   **Conclusion:** Based on the combined data, we can conclude that house sparrow hotspots in Berlin 
                    demonstrate a high degree of resilience to moderate air pollution. While extreme daily pollution shocks can 
                    lead to temporary declines in observations, the overall population density at these hotspots only suffers significantly 
                    under sustained, very high pollution levels.PM2.5 appears to be a more reliable indicator for population stress than NO2, 
                    as the negative impact on average counts becomes clearly measurable once the PM2.5 threshold is breached.
                   """)

        st.info(f"💡 **Critical Threshold:** The dashed white line marks the recommended air quality limit ({bar_threshold} µg/m³ for {bar_pollutant_choice}). Bars in **red** represent pollution levels exceeding this safety limit.")
        
        st.info("💡 **PM2.5** consists of fine inhalable particles (≤ 2.5 µm). These mainly originate from combustion and can penetrate deep into the respiratory system, posing a high health risk.")
        
        st.info("💡 **NO₂ (Nitrogen Dioxide):** Primarily produced by combustion engines (especially diesel) and industrial plants. It is a major cause of respiratory inflammation in birds and humans.")
        
    except Exception as e:
        st.error(f"Error loading Research Question 2: {e}")


if selected == "Research Question 3":
    st.title("Research Question 3")
    st.subheader("How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?")

    file_path_rq3 = "Streamlit/RQ_3/rq_3_richness_sh_data.csv"

    try:
        df_richness = pd.read_csv(file_path_rq3)

        st.subheader("🌍 Species Richness by Area Type")

        fig3 = px.scatter_map(
            df_richness,
            lat="lat",
            lon="lon",
            size="species_richness",
            color="area_type",
            color_discrete_map={
                "urban": "firebrick",
                "rural": "royalblue"
            },
            hover_name="area_type",
            hover_data={
                "lat": False, 
                "lon": False, 
                "species_richness": True
            },
            zoom=7,
            center={"lat": 54.2, "lon": 9.8},
            template="plotly_dark"
        )

        fig3.update_layout(
            paper_bgcolor="#0e1117",
            margin=dict(l=0, r=0, t=30, b=0),
            height=600,
            map_style="carto-darkmatter"
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.success("""
                   **Key observations:** The map of Schleswig-Holstein seems to contain more rural points (blue) than urban ones (red).
                   The rural points, show higher diversity more often, indicated by the size of the point.

                   **Conclusion:** From this Data we can conclude that the bird species richness in Schleswig-Holstein in the last
                   30 days is overall higher in rural areas than in urban areas. Especially nature reserves, where the species richness is very high, contribute greatly to the overall richness of rural areas.
                   """)

        st.info("""
        * 💡**Blue markers** represent rural areas, while **red markers** represent urban locations. 
        * 💡The **size of the circles** corresponds to the species richness (number of different bird species) observed in the last 30 days. 
        * 💡Larger circles indicate a higher biodiversity at the specific coordinate.
        """)

    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 4":
    st.title("Research Question 4")
    st.subheader("How does O3 concentration influence the observation frequency of feral pigeons in Berlin in the years 2021-2024?")

    file_path = "Streamlit/RQ_4/berlin_pigeon_pullution_2020_2024.csv"

    @st.cache_data
    def get_data(path):
        df = pd.read_csv(path, index_col=0)
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")
        df = df[df["O3"] >= 0].copy()
        df["Year"] = df["Date"].dt.year.astype(str)
        
        df["P_7d"] = df["PigeonCount"].rolling(window=7, center=True).mean()        #preparing the smoothing
        df["P_30d"] = df["PigeonCount"].rolling(window=30, center=True).mean()
        df["O_7d"] = df["O3"].rolling(window=7, center=True).mean()
        df["O_30d"] = df["O3"].rolling(window=30, center=True).mean()
        return df

    try:
        df = get_data(file_path)

        st.subheader("🐦 Pigeon Count vs. O3 in Berlin")

        st.subheader("Time Series Analysis")        #first graph
        
        smooth_option = st.radio("Choose smoothing option:", ["Daily", "Weekly (7d)", "Monthly (30d)"], horizontal=True)
        
        p_col = {"Daily": "PigeonCount", "Weekly (7d)": "P_7d", "Monthly (30d)": "P_30d"}[smooth_option]
        o_col = {"Daily": "O3", "Weekly (7d)": "O_7d", "Monthly (30d)": "O_30d"}[smooth_option]


        start_date, end_date = st.slider(       #defining the slider
            "Choose time period:",
            min_value=datetime.datetime(2021, 1, 1),
            max_value=df["Date"].max().to_pydatetime(),
            value=(datetime.datetime(2021, 1, 1), df["Date"].max().to_pydatetime()),
            format="DD.MM.YYYY"
        )

        
        df_filtered = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

        fig1 = make_subplots(specs=[[{"secondary_y": True}]])
        fig1.add_trace(
            go.Scatter(x=df_filtered["Date"], y=df_filtered[p_col], name="Pigeon Count",
                    line=dict(color="royalblue", width=2)), secondary_y=False
        )
        fig1.add_trace(
            go.Scatter(x=df_filtered["Date"], y=df_filtered[o_col], name="O3 Level",
                    line=dict(color="firebrick", dash="dot", width=1.5)), secondary_y=True
        )

        fig1.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            hovermode="x unified",
            margin=dict(l=0, r=0, t=40, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig1, use_container_width=True)

        st.success("""
                   The graph shows the pigeon counts in Berlin in the years 2021-2024 and the O3 concentration per day.

                   **Key observations:** We can better see with the smoothing option "Monthly (30d)" that the pigeon count over
                   all the years follow a pattern of rising about the time, when O3 levels decrease. The pigeon counts generally peak
                   in between the peaks of the O3 level peaks.
                   """)

        st.divider()


        st.subheader("Regression Analysis")     #Second graph 

        available_years = sorted(df["Year"].unique())
        selected_years = st.multiselect("filter years:", available_years, default=available_years)      #multiselect for each year

        df_reg = df[df["Year"].isin(selected_years)]

        if not df_reg.empty:
            try:
                fig2 = px.scatter(
                    df_reg, x="O3", y="PigeonCount", color="Year",
                    trendline="ols", trendline_scope="overall",
                    trendline_color_override="white",
                    opacity=0.5, template="plotly_dark"
                )
                
                fig2.update_layout(
                    paper_bgcolor="#0e1117",
                    plot_bgcolor="#0e1117",
                    xaxis_title="O3 Concentration (µg/m³)",
                    yaxis_title="Pigeon Count"
                )
                fig2.update_xaxes(range=[0, df["O3"].max() * 1.05])
                fig2.update_yaxes(range=[0, 130])

                st.plotly_chart(fig2, use_container_width=True)

                st.success("""
                           This graph shows similar to the first graph the pigeon counts on the y-axis and the O3 concentration on the x-axis.

                           **Key observations:** The first and the second graph are in an agreement that a slight negative correlation exists,
                           between pigeon counts in Berlin and the O3 concentration, as indicated by the white line.
                           """)

                
            except Exception as inner_e:
                st.error("The graph cannot be displayed.")
        else:
            st.warning("Please choose at least one year.")

        st.divider()
        st.subheader("Distribution Analysis")       #third graph

        bin_edges = list(range(0, 111, 10))
        df_binned = df.copy()
        df_binned["O3_Bin"] = pd.cut(df_binned["O3"], bins=bin_edges)
        
        df_hist_plot = df_binned.groupby("O3_Bin", observed=True).agg({
            "PigeonCount": "sum"
        }).reset_index()

        df_hist_plot["O3_Range"] = df_hist_plot["O3_Bin"].astype(str)


        fig3 = px.bar(
            df_hist_plot,
            x="O3_Range",
            y="PigeonCount",
            title="<b>Total Pigeon Counts per O3 Concentration Range</b>",
            labels={
                "O3_Range": "O3 Concentration (µg/m³)",
                "PigeonCount": "Total Pigeon Count"
            },
            template="plotly_dark",
            color_discrete_sequence=["royalblue"]
        )

        fig3.update_layout(
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            bargap=0.1,
            xaxis={
                'title': 'O3 Concentration (µg/m³)',
                'categoryorder': 'array', 
                'categoryarray': df_hist_plot["O3_Range"]
            },
            yaxis_title="Total Pigeons Counted"
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.success("""
                   This Histogram, displays the distribution of pigeons in certain O3 concentration ranges.

                   **Key observations:** The most pigeons were seen when the concentration was 20-30 µg/m³ and 50-60µg/m³.

                   **Conclusion:** The graphs, mostly the first and second one, show a slight negative correlation between the pigeon counts
                   and the O3 concentration. So we can say, based on the data, that increasing O3 concentration decreases the amount of
                   feral pigeon observations in Berlin.
                   """)

    except Exception as e:
        st.error(f"Error")
        st.info(f"Details: {e}")

    st.info("💡 **O3 (Ground-level ozone)** is a secondary pollutant formed when sunlight and heat trigger a chemical reaction between precursor pollutants (like vehicle emissions). Therefore, higher temperatures and intense sun lead to higher ozone levels.")


if selected == "Research Question 5":
    st.title("Research Question 5")
    st.subheader("Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?")
    st.subheader("🌍Density vs. stability of Mallard Ducks (2020-2024)")

    try:
        df_hist = pd.read_csv("Streamlit/RQ_5/europe_ducks_march_2020_2024.csv")
        df_density = pd.read_csv("Streamlit/RQ_5/europe_ducks_recent_daily.csv")

        df_hist["Date"] = pd.to_datetime(df_hist["Date"])
        daily_ducks = df_hist.groupby(["Country","Date"])["DuckCount"].sum().reset_index()
        stability = daily_ducks.groupby("Country")["DuckCount"].agg(mean="mean", std="std").reset_index()
        stability["CV"] = stability["std"] / stability["mean"]

        density_country = df_density.groupby("Country").mean(numeric_only=True).reset_index()
        density_country["Density"] = density_country["DuckCount"] / density_country["LocationCount"]

        df_combined = pd.merge(density_country, stability, on="Country", how="left")

        view_option = st.selectbox(
            "Choose the metric for the map:",
            ["Density", "Instability (CV)"]
        )

        target_col = "Density" if view_option == "Density" else "CV"
        color_scale = "Reds" if view_option == "Density" else "Blues"

        fig_map = px.choropleth(
            df_combined,
            locations="Country",
            locationmode="country names",
            color=target_col,
            hover_name="Country",
            hover_data={"Density": ":.2f", "CV": ":.2f"},
            color_continuous_scale=color_scale,
            scope="europe"
        )

        fig_map.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular',
                landcolor="#0e1117",
                showland = True,
                bgcolor="#0e1117",          
                lakecolor="#0e1117"
            ),
            margin=dict(l=0, r=0, t=50, b=0),
            height = 500,
            template="plotly_dark"
        )

        st.plotly_chart(fig_map, use_container_width=True)

        st.success("""
                   This map shows the density of mallard ducks in the last 30 days and the stability of the duck population from
                   2020-2024 of Europe.

                   **Key observations:** The map shows that Poland and Finland have a high density of ducks with a pretty stabkle
                   popuulation. The population of Denmark on the other hand is very unstable and the density is relatively low, possibly
                   because Denmark is just a Seasonal Hotspot for Mallard ducks.
                   """)

        if view_option == "Density":
            st.info("💡 **Density**: Shows where the average duck count per location for each European country.")
        else:
            st.info("💡 **Instability (CV, Coefficient of Variation)**: A high value indicates strong fluctuation over the years (for example: migration). A low value indicates a constant population.")

        st.divider()
        st.subheader("Duck Density vs Stability (Quadrant Analysis)")

        median_density = df_combined["Density"].median()
        median_cv = df_combined["CV"].median()

        def classify(row):
            if row["Density"] >= median_density and row["CV"] <= median_cv:
                return "Stable Core Population"
            elif row["Density"] >= median_density and row["CV"] > median_cv:
                return "Seasonal Hotspot"
            elif row["Density"] < median_density and row["CV"] <= median_cv:
                return "Small Stable Population"
            else:
                return "Random Observations"

        df_combined["Category"] = df_combined.apply(classify, axis=1)

        x_max = df_combined["Density"].max() * 1.1
        y_max = df_combined["CV"].max() * 1.1

        fig_quad = px.scatter(
            df_combined,
            x="Density",
            y="CV",
            color="Category",
            text="Country",
            size="mean",
            hover_name="Country",
            hover_data=["Density","CV","mean","std"],
            template="plotly_dark",
            color_discrete_map={
                "Stable Core Population": "#1C7A24",
                "Seasonal Hotspot": "#E67E22",
                "Small Stable Population": "royalblue",
                "Random Observations": "firebrick"
            }
        )

        fig_quad.update_traces(textposition="top center")
        fig_quad.add_vline(x=median_density, line_dash="dash", line_color="grey")
        fig_quad.add_hline(y=median_cv, line_dash="dash", line_color="grey")

        fig_quad.update_layout(
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            height=600,
            xaxis=dict(range=[0, x_max]),
            yaxis=dict(range=[0, y_max]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            updatemenus=[
                dict(
                    type="dropdown",
                    direction="down",
                    x=0.01,
                    y=1.15,
                    showactive=True,
                    buttons=[
                        dict(
                            label="Show All Regions",
                            method="relayout",
                            args=[{"xaxis.range": [0, x_max], "yaxis.range": [0, y_max]}]
                        ),
                        dict(
                            label="Zoom: Stable & Dense",
                            method="relayout",
                            args=[{"xaxis.range": [median_density, x_max], "yaxis.range": [0, median_cv]}]
                        ),
                        dict(
                            label="Zoom: Unstable & Dense",
                            method="relayout",
                            args=[{"xaxis.range": [median_density, x_max], "yaxis.range": [median_cv, y_max]}]
                        ),
                        dict(
                            label="Zoom: Stable & Sparse",
                            method="relayout",
                            args=[{"xaxis.range": [0, median_density], "yaxis.range": [0, median_cv]}]
                        ),
                        dict(
                            label="Zoom: Unstable & Sparse",
                            method="relayout",
                            args=[{"xaxis.range": [0, median_density], "yaxis.range": [median_cv, y_max]}]
                        ),
                    ]
                )
            ]
        )

        st.plotly_chart(fig_quad, use_container_width=True)

        st.success("""
                   Here we can see a Quadrant Analysis of each European country with data of the density and stability in four 
                   different categories.

                   **Key observations:** Most of the countries are relatively stable with a lower density of Mallard ducks. Like mentioned
                   before: Finland, Poland and Denmark are visible outliers in the data.

                    **Conclusion:** The data shows that Poland and Finland are the main hub of the Mallard ducks, followed by Sweden and Hungary.
                   """)

        st.info("""
        * **Stable Core (Green):** High numbers, low fluctuation. These countries are the heart of the population.
        * **Seasonal Hotspot (Orange):** High numbers but high fluctuation. Typical for countries birds only visit during migration.
        * **Small Stable (Blue):** Lower numbers, but they stay constant.
        * **Random Observations (Red):** Low numbers and unpredictable.
        """)

    except Exception as e:
        st.error(f"Error:")
        st.exception(e) 


if selected == "Research Question 6":
    st.title("Research Question 6")
    st.subheader("How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany?")
    st.subheader("☀️Bird species richness vs. Temperature (North vs. South)")

    file_path_rq6 = "Streamlit/RQ_6/final_richness_vs_temp.csv"

    try:
        df_richness = pd.read_csv(file_path_rq6)

        df_richness["Region"] = df_richness["Region"].replace({"Nord": "North", "Süd": "South"})

        bins = [-5, 0, 5, 10, 15, 20, 25, 30]
        bin_labels = ['<0°C', '0-5°C', '5-10°C', '10-15°C', '15-20°C', '20-25°C', '25-30°C']
        
        df_richness['Temp_Group'] = pd.cut(
            df_richness['Max_Temp'], 
            bins=bins, 
            labels=bin_labels
        )

        view_option = st.selectbox(         #interactivity
            "Select region filter:",
            ["Show Both", "North Only", "South Only"]
        )
       
        if view_option == "North Only":
            df_plot = df_richness[df_richness["Region"] == "North"]
        elif view_option == "South Only":
            df_plot = df_richness[df_richness["Region"] == "South"]
        else:
            df_plot = df_richness

        df_grouped = df_plot.groupby(
            ['Temp_Group', 'Region'], 
            observed=False
        )['SpeciesRichness'].mean().reset_index()

        fig6 = px.bar(
            df_grouped,
            x="Temp_Group",
            y="SpeciesRichness",
            color="Region",
            barmode="group",
            title="",
            labels={
                "Temp_Group": "Temperature Range",
                "SpeciesRichness": "Avg. Number of Species",
                "Region": "Location"
            },
            color_discrete_map={"North": "royalblue", "South": "firebrick"},
            template="plotly_dark"
        )

        fig6.update_layout(
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            margin=dict(t=50, b=50),
            height=600
        )

        st.plotly_chart(fig6, use_container_width=True)

        st.success("""
               This comparitve analysis shows the bird species richness for Northern and Southern Germany for different temperatures. 
               It reveals that Southern Germany has a significantly higher biodiversity across the entire temperature spectrum 
               compared to Northern Germany.
               """)

    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 7":
    st.title("Research Question 7")
    st.subheader("How does wind speed affect the observation frequency of duck species?")
    st.subheader("🦆Duck species vs. Wind speeds (North vs. South)")

    file_path_rq7 = "Streamlit/RQ_7/analyse_wind_enten_deutschland.csv"

    try:
        df_wind = pd.read_csv(file_path_rq7)
        df_wind['wind_rounded'] = df_wind['wind_speed'].round(0)
        df_wind['region'] = df_wind['region'].replace({"Nord": "North", "Süd": "South"})

        col1, col2 = st.columns(2)

        with col1:
            view_option = st.selectbox(         #interactivity
                "Filter by Region:",
                ["All Regions", "North Only", "South Only"],
                key="rq7_region_filter"
            )

        with col2:
            all_species = sorted(df_wind['species'].unique())
            selected_species = st.multiselect(          #interactivity
                "Filter by Species:",
                options=all_species,
                default=all_species,
                key="rq7_species_filter"
            )

        if view_option == "North Only":
            df_filtered = df_wind[df_wind["region"] == "North"]
        elif view_option == "South Only":
            df_filtered = df_wind[df_wind["region"] == "South"]
        else:
            df_filtered = df_wind.copy()

        df_filtered = df_filtered[df_filtered["species"].isin(selected_species)]

        if not df_filtered.empty:
            df_avg = df_filtered.groupby(
                ['wind_rounded', 'region', 'species'], 
                observed=False
            )['count'].mean().reset_index()

            fig7 = px.line(
                df_avg,
                x="wind_rounded",
                y="count",
                color="species",
                line_dash="region",
                title=f"Average Duck Count vs. Wind Speed",
                labels={
                    "wind_rounded": "Wind Speed (km/h)",
                    "count": "Avg. Number of Individuals",
                    "species": "Species",
                    "region": "Region"
                },
                color_discrete_map={
                    "Mallard": "firebrick",
                    "Tufted Duck": "royalblue",
                    "Eurasian Wigeon": "#1C7A24"
                },
                template="plotly_dark"
            )

            fig7.update_layout(
                paper_bgcolor="#0e1117",
                plot_bgcolor="#0e1117",
                hovermode="x unified",
                height=600,
            )

            fig7.update_traces(line_shape='spline')     #smoothing the curves

            st.plotly_chart(fig7, use_container_width=True)
            
        else:
            st.warning("No data found for the selected combination of filters.")

        st.success("""
            This visualization examines the correlation between wind speed and observation counts for three distinct 
            duck species across Northern and Southern Germany. While a general linear correlation is weak,
            a visible peak in Tufted Duck and Eurasian Wigeon sightings occurs at 40 km/h in Southern Germany.
            Aside from this specific peak, data suggest only a marginal increase in observations as wind speed inceases.
            """)

    except Exception as e:
        st.error(f"Error loading Research Question 7: {e}")


if selected == "Research Question 8":
    st.title("Research Question 8")
    st.subheader("How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2024?")
    st.subheader("🍃🍂Comparison of Migratory Bird Patterns in Schleswig-Holstein (Spring vs. Autumn)")

    file_path_rq8 = "Streamlit/RQ_8/migratory_observations_SH_2021-2025.csv"

    species_translation = {
        "Weißwangengans": "Barnacle Goose",
        "Knutt": "Red Knot",
        "Ringelgans": "Brant Goose",
        "Alpenstrandläufer": "Dunlin",
        "Austernfischer": "Oystercatcher"
    }

    try:
        df_mig = pd.read_csv(file_path_rq8)

        df_mig['Species'] = df_mig['Species'].replace(species_translation)
        
        target_years = [2021, 2024]
        target_seasons = ['Spring', 'Autumn']
        
        df_filtered = df_mig[
            df_mig['Year'].isin(target_years) & 
            df_mig['Season'].isin(target_seasons)
        ].copy()
        
        df_grouped = df_filtered.groupby(
            ['Year', 'Season', 'Species'], 
            observed=False
        )['Count'].sum().reset_index()

        colors = [
            "firebrick", 'royalblue', '#E67E22', '#1C7A24', 
            '#8E44AD', '#F1C40F', '#2E86C1', '#C0392B'
        ]

        view_mode = st.radio(
            "Select Visualization Mode:",
            ["Side-by-Side Comparison", "Full Hierarchy (Combined)"],
            horizontal=True
        )

        if view_mode == "Side-by-Side Comparison":
            fig8 = make_subplots(
                rows=1, cols=2, 
                specs=[[{"type": "sunburst"}, {"type": "sunburst"}]],
                subplot_titles=("Year: 2021", "Year: 2024")
            )

            def create_trace(data, path):
                temp_fig = px.sunburst(
                    data, path=path, values='Count', 
                    color_discrete_sequence=colors
                )
                trace = temp_fig.data[0]
                trace.insidetextorientation = 'horizontal'
                trace.textinfo = "label+percent parent"
                trace.marker.colors = colors * 10 
                return trace

            trace_2021 = create_trace(df_grouped[df_grouped['Year'] == 2021], ['Season', 'Species'])
            trace_2024 = create_trace(df_grouped[df_grouped['Year'] == 2024], ['Season', 'Species'])

            fig8.add_trace(trace_2021, row=1, col=1)
            fig8.add_trace(trace_2024, row=1, col=2)
            
        else:
            fig8 = px.sunburst(
                df_grouped, 
                path=['Year', 'Season', 'Species'], 
                values='Count', 
                color_discrete_sequence=colors
            )
            fig8.update_traces(
                insidetextorientation='horizontal',
                textinfo="label+percent parent",
                marker=dict(line=dict(color='white', width=1.5))
            )

        fig8.update_layout(
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            font=dict(color="white"),
            height=700,
            margin=dict(t=80, l=10, r=10, b=10)
        )

        st.plotly_chart(fig8, use_container_width=True)

        st.success("""
               This Visulaization compares the relative amounts of migratory bird observations between 2021 and 2024.
               The Barnacle Goose remains the most dominant species in both periods. However, a 
               significant change is observed in the Red Knot: while observations peaked during the spring of 
               2021, the 2024 data shows a transition toward an autumn-heavy distribution. While most species 
               remained consistent in their timing, specific shifts show the dynamic nature of migratory birds.
               """)

        st.info("💡**How to use:** Click on the inner rings (Year or Season) to zoom into specific data segments.")

    except Exception as e:
        st.error(f"Error loading Research Question 8: {e}")


if selected == "Research Question 9":
    st.title("Research Question 9")
    st.subheader("Did Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?")
    st.subheader("𓅰 𓅬 𓅭 𓅮 𓅯Migration vs. Air Pollution")
    st.subheader("Boxplot: PM10 vs. PM2.5 vs. O3 comparison")

    file_path_rq9 = "Streamlit/RQ_9/craneCount_pollution_arrivalDates_2021-2025.csv"

    try:
        df_cranes = pd.read_csv(file_path_rq9)
        df_cranes['Date'] = pd.to_datetime(df_cranes['Date'])
        
        df_cranes['Is_Arrival_Day'] = df_cranes['Is_Arrival_Day'].astype(str).str.lower().str.strip()
        df_cranes = df_cranes[df_cranes['Date'].dt.month <= 4].copy()

        df_cranes['Category'] = 'Rest of the time'
        df_cranes.loc[df_cranes['Is_Arrival_Day'] == 'yes', 'Category'] = 'Arrival Day'

        arrival_dates = df_cranes[df_cranes['Is_Arrival_Day'] == 'yes']['Date'].unique()
        for arrival_date in arrival_dates:
            mask = (df_cranes['Date'] >= arrival_date - pd.Timedelta(days=14)) & (df_cranes['Date'] < arrival_date)
            df_cranes.loc[mask & (df_cranes['Category'] == 'Rest of the time'), 'Category'] = '14 Days before arrival'

        pollutant = st.selectbox(       #interaction
            "Select pollutant to analyze:",
            ["PM10", "PM2.5", "O3"]
        )

        fig = go.Figure()

        categories = ['Rest of the time', '14 Days before arrival', 'Arrival Day']
        colors = ["#bdc3c7", "royalblue", "firebrick"]

        for i, cat in enumerate(categories):
            plot_data = df_cranes[df_cranes['Category'] == cat][pollutant]
            
            fig.add_trace(go.Box(
                y=plot_data,
                name=cat,
                marker=dict(color='white', opacity=0.7, size=10),
                line=dict(width=2),
                fillcolor=colors[i],
                boxpoints='all',
                jitter=0.3,       
                pointpos=0,
                showlegend=False
            ))

       
        fig.update_layout(
            title=f"Concentration of {pollutant} (January - April)",
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            yaxis_title="Concentration (µg/m³)",
            xaxis=dict(type='category'),
            boxgap=0.2,
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

        st.success("""
                   This boxplot shows the concentrations of PM10, PM2.5, and O3 categorized by crane arrival events from 
                   January to April. The data shows a rise on and before arrival days in PM10 and PM2.5 and a drop in O3. 
                   However, these trends should be interpreted with caution, as the 'Arrival Day' category represents 
                   only five data points, while the 'Rest of the time' has significantly more.
               """)

        st.divider()
        st.subheader("Time Series: PM10 Concentration vs. Crane Observations")          #second graph

        df_ts = df_cranes.copy().sort_values("Date")
        
        df_ts['PM10_smooth'] = df_ts['PM10'].rolling(window=14, center=True).mean()
        df_ts['Count_smooth'] = df_ts['Count'].rolling(window=14, center=True).mean()

        fig9_ts = make_subplots(specs=[[{"secondary_y": True}]])

        fig9_ts.add_trace(
            go.Scatter(
                x=df_ts["Date"], 
                y=df_ts["PM10_smooth"], 
                name="PM10 Concentration (Smooth)",
                line=dict(color="firebrick", width=2)
            ), 
            secondary_y=False
        )

        fig9_ts.add_trace(
            go.Scatter(
                x=df_ts["Date"], 
                y=df_ts["Count_smooth"], 
                name="Crane Count (Smooth)",
                line=dict(color="royalblue", width=2)
            ), 
            secondary_y=True
        )

        fig9_ts.update_layout(
            title="<b>14-Day Rolling Average: PM10 vs. Crane Counts</b>",
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        fig9_ts.update_yaxes(title_text="PM10 (µg/m³)", secondary_y=False, color="firebrick")
        fig9_ts.update_yaxes(title_text="Crane Count", secondary_y=True, color="royalblue")

        st.plotly_chart(fig9_ts, use_container_width=True)

        st.success("""
                   This time-series analysis displays the smoothed observation counts of cranes alongside PM10 
                   concentrations from 2021 to 2025. 
                   A seasonal synchronicity is evident, as both variables reach their peak during 
                   spring of each year. 
               """)
        
        st.divider()
        st.subheader("Seasonal Comparison: Annual Arrival Patterns & PM10")

        df_overlay = df_cranes.copy()
        df_overlay['Year'] = df_overlay['Date'].dt.year
        df_overlay['Month'] = df_overlay['Date'].dt.month
        df_overlay['DayOfYear'] = df_overlay['Date'].dt.dayofyear
        df_overlay = df_overlay[df_overlay['Month'] <= 3].copy()

        df_overlay['Count_Smooth'] = df_overlay.groupby('Year')['Count'].transform(lambda x: x.rolling(window=7, center=True).mean())
        df_overlay['PM10_Smooth'] = df_overlay.groupby('Year')['PM10'].transform(lambda x: x.rolling(window=7, center=True).mean())
        df_overlay['DummyDate'] = df_overlay['Date'].apply(lambda x: x.replace(year=2024))

        available_years = sorted(df_overlay['Year'].unique())
        selected_years = st.multiselect(
            "Select years to compare:",
            options=available_years,
            default=available_years,
            key="rq9_year_filter"
        )

        df_filtered_years = df_overlay[df_overlay['Year'].isin(selected_years)].copy()

        if not df_filtered_years.empty:
            avg_data = df_overlay.groupby('DayOfYear').agg({
                'PM10_Smooth': 'mean', 
                'Count_Smooth': 'mean', 
                'DummyDate': 'first'}).reset_index()
            
            fig9_overlay = make_subplots(specs=[[{"secondary_y": True}]])
            strong_palette = ['royalblue', 'firebrick', '#1C7A24', '#E67E22', '#8E44AD']
            
            for i, year in enumerate(selected_years):
                yearly_df = df_filtered_years[df_filtered_years['Year'] == year].sort_values('DayOfYear')
                color = strong_palette[i % len(strong_palette)]
                
                fig9_overlay.add_trace(
                    go.Scatter(x=yearly_df['DummyDate'], y=yearly_df['Count_Smooth'], 
                               name=f'Cranes {year}', 
                               line=dict(color=color, width=2.5),
                               legendgroup=f'group{year}',
                               showlegend=True),
                    secondary_y=True
                )
                
                fig9_overlay.add_trace(
                    go.Scatter(x=yearly_df['DummyDate'], y=yearly_df['PM10_Smooth'], 
                               name=f'PM10 {year} (dot)', 
                               line=dict(color=color, width=1.3, dash='dot'),
                               opacity=0.5, 
                               legendgroup=f'group{year}',
                               showlegend=True),
                    secondary_y=False
                )
                
                arrivals = yearly_df[yearly_df['Is_Arrival_Day'].astype(str).str.lower().str.strip() == 'yes']
                fig9_overlay.add_trace(
                    go.Scatter(x=arrivals['DummyDate'], y=arrivals['Count_Smooth'],
                               mode='markers', 
                               name=f'Arrival {year} (★)',
                               marker=dict(symbol='star', size=11, color=color, 
                                         line=dict(width=1, color='white')),
                               legendgroup=f'group{year}',
                               showlegend=True),
                    secondary_y=True
                )

            fig9_overlay.add_trace(
                go.Scatter(x=avg_data['DummyDate'], y=avg_data['Count_Smooth'], 
                           name='Ø General Trend', 
                           line=dict(color='white', width=3),
                           legendgroup='avg',
                           showlegend=True),
                secondary_y=True)

            fig9_overlay.update_layout(
                title='<b>Seasonal Comparison: Annual Comparison (Jan - Mar)</b>',
                xaxis_title='Timeline (January to March)',
                xaxis=dict(tickformat='%b', range=['2024-01-01', '2024-03-31']),
                hovermode='x unified',
                template="plotly_dark",
                paper_bgcolor="#0e1117",
                plot_bgcolor="#0e1117",
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.05, traceorder="grouped"),
                height=700
            )

            fig9_overlay.update_yaxes(title_text="PM10 Concentration", secondary_y=False)
            fig9_overlay.update_yaxes(title_text="Crane Count", secondary_y=True)

            st.plotly_chart(fig9_overlay, use_container_width=True)
        else:
            st.warning("Please select at least one year to display the comparison.")

        st.success("""
                  This visualization shows crane observation counts and PM10 concentrations from 2021 to 2025 (January-April), 
               with the specific arrival dates highlighted by star markers.
                   
               **Conclusion:** The arrival dates remain almost consistent each year. Furthermore, the peaks in PM10 levels frequently happen 
               either immediately before or after the peak in crane sightings. The cranes seem to be indifferent regarding the higher pollution levels,
                   they arrive either way at around the middle of February
                   """)
        
        st.info("💡 **PM10** refers to coarse inhalable particles with diameters generally 10 micrometers and smaller. These are often produced by mechanical processes like road dust resuspension, construction work, and industrial activities. They can irritate the eyes and upper respiratory tract.")
        st.info("💡 **PM2.5** consists of fine inhalable particles with diameters of 2.5 micrometers and smaller. These tiny particles mainly originate from combustion processes (e.g. vehicle engines, wood burning). Because of their size, they can penetrate deep into the lungs and even enter the bloodstream, posing a higher health risk to wildlife and humans.")
        st.info("💡 **O3 (Ground-level ozone)** is a secondary pollutant formed when sunlight and heat trigger a chemical reaction between precursor pollutants (like vehicle emissions). Therefore, higher temperatures and intense sun lead to higher ozone levels.")
        st.info(""" 
**💡Crane Migration:** Cranes arriving in Lower Saxony typically follow the **Western European fly route**. 
* **From France:** Birds departing from France can reach Germany in just 1-2 days of continuous flight. 
* **From Spain:** Cranes from Spain often take about 2 weeks for the entire journey, including essential rest stops in France to refuel.
* **Relevance:** This is why we analyze pollution levels up to 14 days before arrival, as air quality could theoretically influence their timing and stamina in this time window.""")
    except Exception as e:
        st.error(f"Error loading Research Question 9: {e}")
