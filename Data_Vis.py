from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('Data_processing.csv')        
df['Date'] = pd.to_datetime(df['Date'])        # Convert Date column to datetime type
df = df.sort_values('Date')                    


app = Dash(__name__)


colors = {
    'background': "#292929",   
    'text': "#CAF0FF"          
}


app.layout = html.Div(
    style={
        'backgroundColor': colors['background'],  # Set background color
        'color': colors['text'],                  # Set text color
        'padding': '20px'                         # Add padding for spacing
    },
    children=[
        # Title
        html.H1(
            children='Soul Foods Sales Visualiser',
            style={'textAlign': 'center'}          # Center align title
        ),

        # Subtitle / description
        html.Div(
            children='Visualising sales before and after the Pink Morsel price increase',
            style={'textAlign': 'center'}          # Center align subtitle
        ),

        # Region filter (Radio buttons)
        html.Div([
            html.Label(
                "Select Region:", 
                style={"fontWeight": "bold", "marginRight": "10px"}  # Label style
            ),
            dcc.RadioItems(
                id="region-filter",  # it’s a unique identifier in a Dash application. Used To link a dropdown, button, graph, or input to a callback function
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"}
                ],
                value="all",          # Default option
                inline=True,          # Display horizontally (side by side)
                style={"marginBottom": "20px"}
            )
        ], style={"textAlign": "center"}),  # Center the radio buttons

        
        dcc.Graph(id='sales-line-chart')
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),    # Output: updates the chart
    Input("region-filter", "value")          # Input: listens to region selection
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]  

    # Create line chart
    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",   # Color-coded by region
        title=f"Sales Trends for {selected_region.capitalize() if selected_region!='all' else 'All Regions'}"
    )

    # Update chart styling
    fig.update_layout(
        plot_bgcolor=colors['background'],    
        paper_bgcolor=colors['background'],   
        font_color=colors['text'],            
        title_x=0.5                           
    )

    return fig  


if __name__ == '__main__':
    app.run(debug=True)  
