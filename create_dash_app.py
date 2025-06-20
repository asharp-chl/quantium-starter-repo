#create a Dash app to visualise the data from the csv file
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the data
data = pd.read_csv('daily_sales_data.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Create the line chart
fig = px.line(data, 
              x='date', 
              y='sales',
              title='Daily Sales of Pink Morsels',
              labels={'date': 'Date', 'sales': 'Sales ($)'})

# Define the layout
app.layout = html.Div([
    html.H1('Pink Morsel Sales Dashboard',
            style={'textAlign': 'center', 'color': '#2c3e50', 'padding': '20px'}),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
