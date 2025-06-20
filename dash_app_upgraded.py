import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the data
data = pd.read_csv('daily_sales_data.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Define colors and styles
colors = {
    'background': '#f4f7fa',
    'text': '#2e3e4e',
    'accent': '#d64541',
    'card_bg': '#ffffff',
    'border': '#e1e8ed',
    'hover': '#f7c6c5'
}

# Common card style
card_style = {
    'backgroundColor': colors['card_bg'],
    'borderRadius': '12px',
    'boxShadow': '0 4px 12px rgba(0,0,0,0.07)',
    'padding': '25px',
    'margin': '20px auto',
    'maxWidth': '900px'
}

# Layout
app.layout = html.Div([
    html.Header([
        html.H1('Pink Morsel Sales Dashboard', 
                style={
                    'textAlign': 'center',
                    'color': colors['accent'],
                    'fontFamily': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
                    'fontWeight': '700',
                    'fontSize': '3.2rem',
                    'marginBottom': '8px',
                    'paddingTop': '40px'
                }),
        html.Div(style={
            'height': '4px',
            'width': '120px',
            'backgroundColor': colors['accent'],
            'margin': '0 auto 40px auto',
            'borderRadius': '4px'
        })
    ]),
    
    html.Section([
        html.Label('Select Region:', 
                   htmlFor='region-selector',
                   style={
                       'fontSize': '1.25rem',
                       'fontWeight': '600',
                       'color': colors['text'],
                       'display': 'block',
                       'marginBottom': '12px'
                   }),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '25px', 'cursor': 'pointer', 'fontSize': '1rem', 'color': colors['text']},
            inputStyle={'marginRight': '6px', 'cursor': 'pointer'}
        )
    ], style=card_style),

    html.Section([
        dcc.Graph(id='sales-line-chart')
    ], style=card_style)
], style={
    'backgroundColor': colors['background'],
    'minHeight': '100vh',
    'padding': '0 20px 40px 20px',
    'fontFamily': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
})

# Callback to update the chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_graph(selected_region):
    filtered_data = data if selected_region == 'all' else data[data['region'] == selected_region]
    
    fig = px.line(
        filtered_data,
        x='date',
        y='sales',
        title=f'Daily Sales of Pink Morsels - {selected_region.title()} Region',
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        template='seaborn'
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        title_x=0.5,
        title_font_size=26,
        font_family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        font_color=colors['text'],
        title_font_color=colors['accent'],
        margin=dict(t=60, b=40, l=50, r=50),
        hovermode='x unified',
        xaxis=dict(
            showgrid=True,
            gridcolor='#e5e5e5',
            linecolor='#cccccc',
            tickangle=-45,
            tickfont=dict(size=11),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#e5e5e5',
            linecolor='#cccccc',
            tickfont=dict(size=11),
        )
    )
    
    fig.update_traces(line=dict(width=1, color=colors['accent']), marker=dict(size=6))
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
