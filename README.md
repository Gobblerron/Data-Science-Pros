# ReadME

**Introduction**

Bird obseravtions provide valuable information about species distribution and environmental changes. Large datasets of bird sighting can help researchers understand ecological trends. This project analysis bird observation data to gain insights into bird activity and distribution.

**Research Questions**

1. How does air Pollution affect bird observation frequency in Hamburg in the years 2021-2025 and which pollutant affects the birds the most?

2. How are hotspots of house sparrows in Berlin influenced by increased pollution in the years 2023-2025?

3. How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?

4. How does O3 concentration influence the observation frequency of feral pigeons in Berlin in the years 2021-2024?

5. Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?

6. How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany?

7. How does wind speed affect the observation frequency of duck species?

8. How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2024?

9. Did Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?

**Data Pipeline**

1. Data Collection:
Bird observation data was collected using the eBird API. This includes information such as species name, observation date and location.
Pollution Data like PM 2.5/10, O3 and NO2 was collected using OpenWeather API. The Visual Crossing API provides wind speed and temperature data. Open-Meteo Archive API was used to retrieve historic weather data, including daily maximum wind speed and temperature.

3. Data Preprocessing:
The collected datasets were cleaned and prepared for the data analysation. This included the selection of relevant features, formatting locations and timestamps. Regarding research question 3 a classification into urban and rural areas was processed. Therefore OpenStreetMap libary was used for analysing a 100-meter radius around each observation location. Then bird observation data was merged with weather and pollution data on features like date and location.

4. Data Storage:
The processed data is stored in CSV format.

5. Data Analysis and Visualisation:
The procesed data was analysed using Python and libararies like Pandas and Numpy.
Plotly was used for visualisation.

**Building and deployement of the website**

The website was built and deployed using Streamlit. The entire code is contained within a single streamlit_app.py file in our repository. This file includes the navigation menu, the individual sections, and the code for all visualizations.

To build the website, we relied on the official Streamlit documentation as well as LLMs like Google Gemini and ChatGPT. We utilized LLMs for some parts of the code due to the four week time constraint and a lack of prior experience in web development.

The deployment of the website was carried out as follows:
First, we connected our GitHub repository to the Streamlit Cloud and authorized the connection. We then created a requirements.txt file in the same directory as streamlit_app.py, listing all the libraries used in the code. Finally, the website was successfully deployed.

**Showcase how to use the website and highlights**

The website is designed for easy usabilty and intuitive interactivity. 
Users can navigate the platform through the sidebar to the following sections:

- **Main Dashboard**: Upon arrival, the homepage shows bird pictures and introduces the Research Questions. It also has our Imprint at the bottom of the page, ensuring transparency regarding the project's academic background and contributors.
- **Data & Sources**: Through the sidebar, the user can visit the Data & Sources page, which provides direct access to our Data Acquisition section. This area explains our methodology and the specific APIs used for this study.
- **Research Questions**: The sidebar allows users to navigate to a page for each Research Question, allowing users to learn more about specific correlations like wind speed impact on duck sightings or the relationship between air quality and crane arrivals.

The main highlights of the website include the interactive visualizations, which allow data exploration, and the Duck Button on the Homepage, which plays a nice duck noise.

**Explanation on Marking of Code via LLM**

Throughout the project, our team made use of AI assistance at selected points in the code. All lines and sections that were developed with the help of an LLM are marked accordingly in the code, so they can be clearly identified.

As a team, we aimed to write as much of the code independently as possible. AI assistance was only used when we were stuck or could not move forward on our own — for example when dealing with unfamiliar API structures, unclear syntax or specific function implementations. Each team member handled this individually and marked the relevant parts in their own code.

Overall, the core logic of the data pipeline and the structure of the scripts were developed by the team itself. The LLM served as a support tool to help us get unstuck, not as the primary author of the code
