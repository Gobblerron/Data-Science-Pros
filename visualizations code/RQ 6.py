import pandas as pd
import plotly.express as px


def visualize_species_richness(csv_file):
    """
    Analyzes and visualizes species richness in relation to temperature groups
    for Northern and Southern regions.
    """
    # 1. Data Loading and Preprocessing
    # Read the dataset containing species richness and temperature data
    df = pd.read_csv(csv_file)

    # Standardize regions for international presentation
    df["Region"] = df["Region"].replace({"Nord": "North", "Süd": "South"})

    # 2. Feature Engineering: Temperature Binning
    # Categorize maximum temperatures into 5-degree intervals for trend analysis
    bins = [-5, 0, 5, 10, 15, 20, 25, 30]
    bin_labels = [
        '<0°C', '0-5°C', '5-10°C', '10-15°C', 
        '15-20°C', '20-25°C', '25-30°C'
    ]
    
    df['Temp_Group'] = pd.cut(
        df['Max_Temp'], 
        bins=bins, 
        labels=bin_labels
    )

    # 3. Aggregation
    # Calculate mean species richness per temperature group and region
    df_grouped = df.groupby(
        ['Temp_Group', 'Region'], 
        observed=False
    )['SpeciesRichness'].mean().reset_index()

    # 4. Visualization Construction
    # Grouped bar charts allow for a direct side-by-side regional comparison
    fig = px.bar(
        df_grouped,
        x="Temp_Group",
        y="SpeciesRichness",
        color="Region",
        barmode="group",
        title="Average Species Richness: North vs. South Comparison",
        labels={
            "Temp_Group": "Temperature Range",
            "SpeciesRichness": "Avg. Number of Species",
            "Region": "Location"
        },
        # Defined aesthetic color mapping for regional distinction
        color_discrete_map={"North": "#FFB7CE", "South": "#C3B1E1"},
        template="plotly_white"
    )

    # 5. Interactive Layout Adjustments
    # AI assistance was utilized to implement the interactive visibility toggle
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "label": "Show Both",
                        "method": "update",
                        "args": [{"visible": [True, True]}]
                    },
                    {
                        "label": "North Only",
                        "method": "update",
                        "args": [{"visible": [True, False]}]
                    },
                    {
                        "label": "South Only",
                        "method": "update",
                        "args": [{"visible": [False, True]}]
                    }
                ],
                "direction": "down",
                "showactive": True,
                "x": 0.0,
                "y": 1.2
            }
        ],
        margin=dict(t=100)
    )

    fig.show()


if __name__ == "__main__":
    DATA_PATH = "final_richness_vs_temp.csv"
    visualize_species_richness(DATA_PATH)
