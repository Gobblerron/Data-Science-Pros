import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Bird observations", layout = "wide")

#Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "main menu",
        options = ["Homepage", "Data and sources", "Research Question 1", "Research Question 2", "Research Question 3", "Research Question 4", "Research Question 5", "Research Question 6", "Research Question 7", "Research Question 8", "Research Question 9"],
        icons = ["house", "database", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill"],
        menu_icon ="cast",
        styles={
            "container": {"padding": "5!important", "background-color": "#0e0a4d"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
            "nav-link-selected": {"background-color": "#130068"},
        }
    )

if selected == "Homepage":
    st.title("Bird observations Dashboard")
    st.subheader("Welcome to the website! Click the options to the left to explore the contents") 


if selected == "Data and sources":
    st.title("Data and Sources")

   
    RQ_1 = pd.read_csv("RQ_1/hamburg_birdCounts_pollution_2021-2025.csv")
    st.success("Data Research Question 1:")
    st.write(RQ_1)

   
    RQ_2 = pd.read_csv("RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv")
    st.success("CSV found!")
    st.write(RQ_2)

   
    RQ_3 = pd.read_csv("RQ_3/rq_3_richness_sh_data.csv")
    st.success("CSV found!")
    st.write(RQ_3)

   
    RQ_4 = pd.read_csv("RQ_4/berlin_pigeon_pullution_2020_2024.csv")
    st.success("CSV found!")
    st.write(RQ_4)


    RQ_5 = pd.read_csv("RQ_5/europe_ducks_march_2020_2024.csv")
    st.success("CSV found!")
    st.write(RQ_5)


    RQ_5_2 = pd.read_csv("RQ_5/europe_ducks_recent_daily.csv")
    st.success("CSV found!")
    st.write(RQ_5_2.head())

    RQ_6 = pd.read_csv("RQ_6/....csv")          #ToDo
    st.success("CSV found!")
    st.write(RQ_6.head())

   
    RQ_7 = pd.read_csv("RQ_7/....csv")          #ToDO
    st.success("CSV found!")
    st.write(RQ_7.head())

   
    RQ_8 = pd.read_csv("RQ_8/migratory_observations_SH_2021-2025.csv")
    st.success("CSV found!")
    st.write(RQ_8.head())

   
    RQ_9 = pd.read_csv("RQ_9/craneArrival_pollution_updated.csv")
    st.success("CSV found!")
    st.write(RQ_9.head())


if selected == "Research Question 1":
    st.title("Research Question 1")
    st.subheader("How does air Pollution affect bird observation frequency in Hamburg in the years 2021-2025 and which pollutant affects the birds the most?")


if selected == "Research Question 2":
    st.title("Research Question 2")
    st.subheader("How are hotspots of house sparrows in Berlin influenced by increased pollution in the years 2023-2025?")


if selected == "Research Question 3":
    st.title("Research Question 3")
    st.subheader("How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?")


if selected == "Research Question 4":
    st.title("Research Question 4")
    st.subheader("How does O3 concentration influence the observation frequency of feral pigeons in Berlin in 2020-2024?")


if selected == "Research Question 5":
    st.title("Research Question 5")
    st.subheader("Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?")


if selected == "Research Question 6":
    st.title("Research Question 6")
    st.subheader("How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany")


if selected == "Research Question 7":
    st.title("Research Question 7")
    st.subheader("How does wind speed affect the observation frequency of Mallards in northern and southern Germany between 2020 and 2025, and does wind speed have a similar effect on other duck species?")


if selected == "Research Question 8":
    st.title("Research Question 8")
    st.subheader("How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2025 and can the potential offspring of those birds be determined?")


if selected == "Research Question 9":
    st.title("Research Question 9")

    st.subheader("Does Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?")
