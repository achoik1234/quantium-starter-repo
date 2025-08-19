from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


df = pd.read_csv('Data_processing.csv')

df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')


app = Dash(__name__)
fig = px.line(
    df,
    x='Date',
    y='Sales',
    title='Soul Foods Sales Over Time',
    labels={'Date': 'Date', 'Sales': 'Sales ($)'}
)


app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Visualiser'),
    html.Div(children='Visualising sales before and after the Pink Morsel price increase'),
    dcc.Graph(id='sales-line-chart', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
