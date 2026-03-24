import pandas as pd
import plotly.express as px


def visualize_wind_impact_on_waterfowl(csv_file):
    """
    Analyzes and visualizes the relationship between wind speed 
    and duck populations across different regions.
    """
    # 1. Data Loading and Initial Processing
    # Load dataset and prepare wind speed values for grouping
    df = pd.read_csv(csv_file)
    
    #  §LLM Help: Rounding wind speed to the nearest integer to create manageable data bins
    df['wind_rounded'] = df['wind_speed'].round(0)
    
    # 2. Statistical Aggregation
    # Calculate the mean count per wind speed, region, and species 
    # to smooth out daily fluctuations
    df_avg = df.groupby(
        ['wind_rounded', 'region', 'species'], 
        observed=False
    )['count'].mean().reset_index()

    # 3. Visualization Construction
    # Using distinct colors for species and line styles for regions 
    # to maintain high data ink ratio and clarity
    fig = px.line(
        df_avg,
        x="wind_rounded",
        y="count",
        color="species",
        line_dash="region",
        title="Average Duck Count vs. Wind Speed (2020-2025)",
        labels={
            "wind_rounded": "Wind Speed (km/h)",
            "count": "Avg. Number of Individuals",
            "species": "Species",
            "region": "Region"
        },
        template="plotly_white"
    )

    # 4. Interactive Layout Adjustment
    # §LLM Help: was utilized here to handle the string-parsing logic 
    # for the trace visibility toggle in the dropdown menu
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "label": "All Regions",
                        "method": "update",
                        "args": [{"visible": [True] * len(fig.data)}]
                    },
                    {
                        "label": "North Only",
                        "method": "update",
                        "args": [
                            {
                                "visible": [
                                    "Nord" in trace.name for trace in fig.data
                                ]
                            }
                        ]
                    },
                    {
                        "label": "South Only",
                        "method": "update",
                        "args": [
                            {
                                "visible": [
                                    "Süd" in trace.name for trace in fig.data
                                ]
                            }
                        ]
                    }
                ],
                "direction": "down",
                "showactive": True,
                "x": 0.01,
                "y": 1.15
            }
        ],
        margin=dict(t=100)
    )

    fig.show()


if __name__ == "__main__":
    DATA_PATH = "analyse_wind_enten_deutschland.csv"
    visualize_wind_impact_on_waterfowl(DATA_PATH)
