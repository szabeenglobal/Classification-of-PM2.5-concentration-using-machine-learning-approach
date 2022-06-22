import dash
import pandas as pd
import numpy as np 
import dash_bootstrap_components as dbc
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies  import Input, Output, State
import plotly.express as  px
import os


#------------------ Load Data ------------------#
csv_files_path = os.path.join('data/df_kensington.csv')
df= pd.read_csv(csv_files_path)
df['AQI-PM2.5'] = df['AQI-PM2.5'].astype('category')
df['AirQuality-PM2.5'] = df['AirQuality-PM2.5'].astype('category')


# -------------------------- TEXT ---------------------------- #


dash_text = '''
Air Quality Perdiction App.
'''
#------------------ DASH ------------------#
external_stylesheets=[dbc.themes.LUX]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets, assets_folder='assets' )
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(
        "Air quality data visualization"),

    dbc.Container(
        dbc.Row(
            [dbc.Col(dcc.Graph(id='graph'), width=6),
            dbc.Col(dcc.Graph(id='graph-1'), width=6)]
        )
    )
    ,
    
    html.Label([
        "colorscale", 
        dcc.Dropdown(
            id='colorscale-dropdown',
            clearable=False,
            value='plasma',
            options=[{'label':c, 'value':c}
                    for c in px.colors.named_colorscales()
                    ])
    ])

])

#Define callback to update graph
@app.callback(
    Output(component_id='graph', component_property='figure'),
    Output(component_id='graph-1', component_property='figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
      figure1 = px.histogram(df, x='AirQuality-PM2.5')
      figure2 = px.histogram(df, x='AirQuality-PM2.5')
      return figure1, figure2
# -------------------------- MAIN ---------------------------- #


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)