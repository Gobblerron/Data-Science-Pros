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
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
            "nav-link-selected": {"background-color": "#1d222c"},
        }
    )
#--------------------------
#        HOMEPAGE
#--------------------------
if selected == "Homepage":
    st.title("Bird observations Dashboard")
    st.subheader("Welcome to the website! Click the options to the left to explore the contents") 

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

#--------------------------
#      Data and sources
#--------------------------

if selected == "Data and sources":
    st.title("Data and Sources")
    st.subheader("APIs used: eBird, OpenWeather, VisualCrossing")

   
    RQ_1 = pd.read_csv("Streamlit/RQ_1/hamburg_birdCounts_pollution_2021-2025.csv")
    st.success("Data used for Research Question 1:")
    st.write(RQ_1)

   
    RQ_2 = pd.read_csv("Streamlit/RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv")
    st.success("Data used for Research Question 2:")
    st.write(RQ_2)

   
    RQ_3 = pd.read_csv("Streamlit/RQ_3/rq_3_richness_sh_data.csv")
    st.success("Data used for Research Question 3:")
    st.write(RQ_3)

   
    RQ_4 = pd.read_csv("Streamlit/RQ_4/berlin_pigeon_pullution_2020_2024.csv")
    st.success("Data used for Research Question 4:")
    st.write(RQ_4)


    RQ_5 = pd.read_csv("Streamlit/RQ_5/europe_ducks_march_2020_2024.csv")
    RQ_5_2 = pd.read_csv("RQ_5/europe_ducks_recent_daily.csv")
    st.success("Data used for Research Question 5:")
    st.write(RQ_5)
    st.write(RQ_5_2)

    RQ_6 = pd.read_csv("Streamlit/RQ_6/final_richness_vs_temp.csv")          
    st.success("Data used for Research Question 6:")
    st.write(RQ_6)

   
    RQ_7 = pd.read_csv("Streamlit/RQ_7/analyse_wind_enten_deutschland.csv")         
    st.success("Data used for Research Question 7:")
    st.write(RQ_7)

   
    RQ_8 = pd.read_csv("Streamlit/RQ_8/migratory_observations_SH_2021-2025.csv")
    st.success("Data used for Research Question 8:")
    st.write(RQ_8)

   
    RQ_9 = pd.read_csv("Streamlit/RQ_9/craneArrival_pollution_updated.csv")
    st.success("Data used for Research Question 9:")
    st.write(RQ_9)

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
        bin_labels = pd.Series(bin_left).round(1).astype(str) + "–" + pd.Series(bin_right).round(1).astype(str)

        fig1 = px.bar(
            summary,
            x=bin_mid,
            y="avg_birds",
            text=summary["avg_birds"].round(1).astype(str) + "<br>(" + summary["days"].astype(str) + " days)",
            title=f"Average Bird Observations vs. {pollutant_choice} Levels (Cleaned Data)",
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

        # --- GESTRICHELTE LINIE FÜR DIE LEGENDE ---
        fig1.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='lines',
            line=dict(color='white', width=2, dash='dash'),
            name=f'Critical Threshold ({threshold} µg/m³)',
            showlegend=True
        ))

        # Die tatsächliche vertikale Linie im Chart
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

    file_path_rq2 = "RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv"

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
            marker=dict(size=8, color="royalblue"),
            hovertemplate="<b>Δ House Sparrows</b><br>Date: %{x|%Y-%m-%d}<br>Change: %{y}<extra></extra>"
        ))

        fig2.add_trace(go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["diff_pm2_5_mean"],
            mode="markers",
            name="Δ PM2.5",
            yaxis="y2",
            marker=dict(size=8, color="firebrick", opacity=0.8),
            hovertemplate="<b>Δ PM2.5</b><br>Date: %{x|%Y-%m-%d}<br>Change: %{y:.2f}<extra></extra>"
        ))

        fig2.add_trace(go.Scatter(
            x=df_filtered["date"],
            y=df_filtered["diff_no2_mean"],
            mode="markers",
            name="Δ NO2",
            yaxis="y2",
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
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
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

        st.info("💡 **PM2.5** consists of fine inhalable particles with diameters of 2.5 micrometers and smaller. These tiny particles mainly originate from combustion processes (e.g. vehicle engines, wood burning). Because of their size, they can penetrate deep into the lungs and even enter the bloodstream, posing a higher health risk to wildlife and humans.")
        st.info("💡 **NO₂ (Nitrogen Dioxide):** This gas is an air pollutant primarily produced by combustion engines, especially diesel vehicles, and industrial power plants, which causes respiratory inflammation.")
    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 3":
    st.title("Research Question 3")
    st.subheader("How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?")

    file_path_rq3 = "RQ_3/rq_3_richness_sh_data.csv"

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

        st.info("""
        * 💡**Green markers** represent rural areas, while **purple markers** represent urban locations. 
        * 💡The **size of the circles** corresponds to the species richness (number of different bird species) observed in the last 30 days. 
        * 💡Larger circles indicate a higher biodiversity at the specific coordinate.
        """)

    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 4":
    st.title("Research Question 4")
    st.subheader("How does O3 concentration influence the observation frequency of feral pigeons in Berlin in the years 2020-2024?")

    file_path = "RQ_4/berlin_pigeon_pullution_2020_2024.csv"

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

    except Exception as e:
        st.error(f"Error")
        st.info(f"Details: {e}")

    st.info("💡 **O3 (Ground-level ozone)** is a secondary pollutant formed when sunlight and heat trigger a chemical reaction between precursor pollutants (like vehicle emissions). Therefore, higher temperatures and intense sun lead to higher ozone levels.")


if selected == "Research Question 5":
    st.title("Research Question 5")
    st.subheader("Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?")
    st.subheader("🌍Density vs. stability of Mallard Ducks (2020-2024)")

    try:
        df_hist = pd.read_csv("RQ_5/europe_ducks_march_2020_2024.csv")
        df_density = pd.read_csv("RQ_5/europe_ducks_recent_daily.csv")


        df_hist["Date"] = pd.to_datetime(df_hist["Date"])
        daily_ducks = df_hist.groupby(["Country","Date"])["DuckCount"].sum().reset_index()
        stability = daily_ducks.groupby("Country")["DuckCount"].agg(mean="mean", std="std").reset_index()
        stability["CV"] = stability["std"] / stability["mean"]

        density_country = df_density.groupby("Country").mean(numeric_only=True).reset_index()
        density_country["Density"] = density_country["DuckCount"] / density_country["LocationCount"]

        
        df_map = pd.merge(density_country, stability, on="Country", how="left")

        
        view_option = st.selectbox(
            "Choose the metric for the map:",
            ["Density", "Instability (CV)"]
        )

        target_col = "Density" if view_option == "Density" else "CV"
        color_scale = "Reds" if view_option == "Density" else "Blues"
        label_text = "Density" if view_option == "Density" else "Instability (Coefficient of Variation)"


        fig = px.choropleth(
            df_map,
            locations="Country",
            locationmode="country names",
            color=target_col,
            hover_name="Country",
            hover_data={"Density": ":.2f", "CV": ":.2f"},
            color_continuous_scale=color_scale,
            scope="europe"
        )

        fig.update_layout(
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
            height = 500
        )

        st.plotly_chart(fig, use_container_width=True)

        if view_option == "Density":
            st.info("💡 **Density**: Shows where the average duck count per location for each European country.")
        else:
            st.info("💡 **Instability (CV, Coefficient of Variation)**: A high value indicates strong fluctuation over the years (for example: migration). A low value indicates a constant population.")

    except Exception as e:
        st.error(f"Error:")
        st.exception(e) 


if selected == "Research Question 6":
    st.title("Research Question 6")
    st.subheader("How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany")
    st.subheader("☀️Bird species richness vs. Temperature (North vs. South)")

    file_path_rq6 = "RQ_6/final_richness_vs_temp.csv"

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

    except Exception as e:
        st.error(f"Error: {e}")


if selected == "Research Question 7":
    st.title("Research Question 7")
    st.subheader("How does wind speed affect the observation frequency of duck species?")
    st.subheader("🦆Duck species vs. Wind speeds (North vs. South)")

    file_path_rq7 = "RQ_7/analyse_wind_enten_deutschland.csv"

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

    except Exception as e:
        st.error(f"Error loading Research Question 7: {e}")


if selected == "Research Question 8":
    st.title("Research Question 8")
    st.subheader("How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2025 and can the potential offspring of those birds be determined?")
    st.subheader("🍃🍂Comparison of Migratory Bird Patterns in Schleswig-Holstein (Spring vs. Autumn)")

    file_path_rq8 = "RQ_8/migratory_observations_SH_2021-2025.csv"

    try:
        df_mig = pd.read_csv(file_path_rq8)
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

        st.info("💡**How to use:** Click on the inner rings (Year or Season) to zoom into specific data segments.")

    except Exception as e:
        st.error(f"Error loading Research Question 8: {e}")


if selected == "Research Question 9":
    st.title("Research Question 9")
    st.subheader("Does Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?")
    st.subheader("𓅰 𓅬 𓅭 𓅮 𓅯Migration vs. Air Pollution")
    st.subheader("Boxplot")

    file_path_rq9 = "RQ_9/craneCount_pollution_arrivalDates_2021-2025.csv"

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






