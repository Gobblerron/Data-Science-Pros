import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def visualize_bird_migration_final(csv_file):
    """
    Generates a sunburst visualization to compare bird migration 
    patterns between 2021 and 2024.
    """
    # 1. Data loading and initial filtering
    # Loading dataset and isolating target years and seasons for the study
    df = pd.read_csv(csv_file)
    target_years = [2021, 2024]
    target_seasons = ['Spring', 'Autumn']
    
    df_filtered = df[
        df['Year'].isin(target_years) & 
        df['Season'].isin(target_seasons)
    ].copy()
    
    # Aggregate specimen counts by year, season, and species
    df_grouped = df_filtered.groupby(
        ['Year', 'Season', 'Species'], 
        observed=False
    )['Count'].sum().reset_index()

    # Define a custom aesthetic color palette (Pastel Pinks and Lavenders)
    girly_colors = [
        '#FFB7CE', '#FADADD', '#E6E6FA', '#F88379', 
        '#C3B1E1', '#FF9BAA', '#D8BFD8', '#FFC0CB'
    ]

    # 2. Side-by-Side Subplot Configuration
    # Setup for independent comparison of the two specific years
    fig = make_subplots(
        rows=1, cols=2, 
        specs=[[{"type": "sunburst"}, {"type": "sunburst"}]],
        subplot_titles=("Year: 2021", "Year: 2024")
    )

    def get_styled_trace(data, path):
        """Helper to create standardized sunburst traces with custom styling."""
        temp_fig = px.sunburst(
            data, 
            path=path, 
            values='Count', 
            color_discrete_sequence=girly_colors
        )
        trace = temp_fig.data[0]
        # Standardize text orientation and data labels
        trace.insidetextorientation = 'horizontal'
        trace.textinfo = "label+percent parent"
        trace.marker.colors = girly_colors * 10 
        return trace

    # Generate traces for individual year analysis
    trace_2021 = get_styled_trace(
        df_grouped[df_grouped['Year'] == 2021], 
        ['Season', 'Species']
    )
    trace_2024 = get_styled_trace(
        df_grouped[df_grouped['Year'] == 2024], 
        ['Season', 'Species']
    )

    fig.add_trace(trace_2021, row=1, col=1)
    fig.add_trace(trace_2024, row=1, col=2)

    # 3. Combined Hierarchy View
    # Unified view showing the full hierarchical structure (Year > Season > Species)
    fig_comb = px.sunburst(
        df_grouped, 
        path=['Year', 'Season', 'Species'], 
        values='Count', 
        color_discrete_sequence=girly_colors
    )
    trace_combined = fig_comb.data[0]
    trace_combined.insidetextorientation = 'horizontal'
    trace_combined.textinfo = "label+percent parent"
    trace_combined.visible = False 
    
    fig.add_trace(trace_combined)

    # 4. Interactive Layout and Menu Design
    # AI assistance was utilized here to refine the complex dropdown 
    # update logic and annotation toggling
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "label": "Side-by-Side (2021 vs 2024)",
                        "method": "update",
                        "args": [
                            {"visible": [True, True, False]}, 
                            {
                                "title": "Observations: 2021 and 2024",
                                "annotations": [
                                    {
                                        "text": "Year: 2021", "showarrow": False, 
                                        "x": 0.225, "y": 1.05, "xref": "paper", 
                                        "yref": "paper", "font": {"size": 16}
                                    },
                                    {
                                        "text": "Year: 2024", "showarrow": False, 
                                        "x": 0.775, "y": 1.05, "xref": "paper", 
                                        "yref": "paper", "font": {"size": 16}
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "label": "Full Hierarchy (Combined)",
                        "method": "update",
                        "args": [
                            {"visible": [False, False, True]}, 
                            {
                                "title": "Observations: 2021 and 2024",
                                "annotations": [
                                    {
                                        "text": "Observations: 2021 and 2024", 
                                        "showarrow": False, "x": 0.5, "y": 1.1, 
                                        "xref": "paper", "yref": "paper", 
                                        "font": {"size": 18}
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "direction": "down",
                "x": 0.0,
                "y": 1.25
            }
        ],
        title_text="Observations: 2021 and 2024",
        font=dict(family="Arial", size=14),
        margin=dict(t=170, l=10, r=10, b=10)
    )

    # Final visual refinements for clarity
    fig.update_traces(marker=dict(line=dict(color='white', width=1.5)))
    fig.show()


if __name__ == "__main__":
    DATA_FILE = 'migratory_observations_SH_2021-2025.csv'
    visualize_bird_migration_final(DATA_FILE)
