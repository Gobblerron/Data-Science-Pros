# Data-Science-Pros


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
