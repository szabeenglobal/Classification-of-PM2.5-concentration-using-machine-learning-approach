import dash
import pandas as pd
import numpy as np 
import dash_bootstrap_components as dbc
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies  import Input, Output, State
import plotly.express as  px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


#------------------ Load Data ------------------#
csv_files_path = os.path.join('data/df_kensington.csv')
df= pd.read_csv(csv_files_path)
df['AQI-PM2.5'] = df['AQI-PM2.5'].astype('category')
df['AirQuality-PM2.5'] = df['AirQuality-PM2.5'].astype('category')
figure1 = px.histogram(df, x='AirQuality-PM2.5')


#Code for figure 2
df_17 = df.loc[df['year'] == 2017].mean()
df_18 = df.loc[df['year'] == 2018].mean()
df_19 = df.loc[df['year'] == 2019].mean()
df_20 = df.loc[df['year'] == 2020].mean()
df_21 = df.loc[df['year'] == 2021].mean()
df_year = pd.concat([df_17,df_18,df_19,df_20,df_21 ], axis=1)
df_year = df_year.T
df_year['year'] = df_year['year'].round()

figure2 = go.Figure()
figure2.add_trace(go.Scatter( x= df_year.year, y= df_year['PM2.5 particulate matter (Hourly measured)'], name='PM2.5', mode='lines+markers'))
figure2.add_trace(go.Scatter( x= df_year.year, y= df_year['Ozone'],name='Ozone', mode='lines+markers') )
figure2.add_trace(go.Scatter( x= df_year.year, y= df_year['PM10 particulate matter (Hourly measured)'],name='PM10', mode='lines+markers') )
figure2.add_trace(go.Scatter( x= df_year.year, y= df_year['Nitrogen dioxide'], name='Nitrogen dioxide',mode='lines+markers'))
figure2.update_layout(title='Annual mean concentration trend for four major <br> pollutants from 2017 to 2021', paper_bgcolor='rgba(0,0,0,0)',
plot_bgcolor='rgba(0,0,0,0)')
figure2.update_xaxes(title_text='Year', showline=True, linewidth=2, linecolor='black')
figure2.update_yaxes(title_text='Pollutant concentration (μgm-3)', showline=True, linewidth=2, linecolor='black')
#Code for figure 3
#Figure box plot showing the variation of PM2.5 concentration
figure3 = make_subplots(rows=3, cols=2)
figure3.add_trace(go.Box(x=df.loc[df['year'] == 2017]['month_name'], 
                    y=df.loc[df['year'] == 2017]['PM2.5 particulate matter (Hourly measured)'], name='2017'), row=1, col=1)
#2018

figure3.add_trace(go.Box(x=df.loc[df['year'] == 2018]['month_name'], 
                    y=df.loc[df['year'] == 2018]['PM2.5 particulate matter (Hourly measured)'], name='2018'), row=1, col=2)
#2019
figure3.add_trace(go.Box(x=df.loc[df['year'] == 2019]['month_name'], 
                    y=df.loc[df['year'] == 2019]['PM2.5 particulate matter (Hourly measured)'],name='2019'), row=2, col=1)
figure3.add_trace(go.Box(x=df.loc[df['year'] == 2020]['month_name'], 
                    y=df.loc[df['year'] == 2020]['PM2.5 particulate matter (Hourly measured)'],name='2020'), row=2, col=2)
figure3.add_trace(go.Box(x=df.loc[df['year'] == 2021]['month_name'], 
                    y=df.loc[df['year'] == 2021]['PM2.5 particulate matter (Hourly measured)'], name='2021'), row=3, col=1)

figure3.update_layout(title='PM2.5 concentration in relation to the annual limit value', paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
figure3.add_hline(y=10)

#Code for figure 4

gh = df.loc[df['year'] == 2021].groupby(['month_name', 'AirQuality-PM2.5'])['date'].aggregate('count')
ij = gh.unstack().fillna(np.nan).T
figure4 = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],[{'type':'domain'},{'type':'domain'}]])
figure4.add_trace(go.Pie(labels=ij.index, values= ij.iloc[:, 2], name='Jan', hole=.3), 1, 1)
figure4.add_trace(go.Pie(labels=ij.index, values= ij.iloc[:, 1], name='Feb', hole=.3), 1, 2)
figure4.add_trace(go.Pie(labels=ij.index, values= ij.iloc[:, 3], name='Mar', hole=.3), 2, 1)
figure4.add_trace(go.Pie(labels=ij.index, values= ij.iloc[:, 0], name='Apr', hole=.3), 2, 2)
figure4.update_layout(title='Variation of Air quality index from Jan-Apr 2021', paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
figure4.update_traces(textposition='inside')
figure4.update_layout(uniformtext_minsize=13, uniformtext_mode='hide')
#Code for figure 5 : fig_weekday
# weekday vs weekend

pm_weekday_mean_19 =df.loc[df['year']==2019].groupby(['weekday']).aggregate('mean')
pm_weekday_mean_20 =df.loc[df['year']==2020].groupby(['weekday']).aggregate('mean')
pm_weekday_mean_21 =df.loc[df['year']==2021].groupby(['weekday']).aggregate('mean')
pm_weekday_mean_21
data=pm_weekday_mean_21
fig_weekday = go.Figure()
fig_weekday.add_trace(go.Scatter(x=['Mon', 'Tue', 'Wed', 'Thu','Fri','Sat', 'Sun'], y= [11.8, 10.720358, 9.265890, 10.060724, 9.413379, 10.117090, 11.261292], name='PM2.5-2019',  mode='lines+markers',line = dict(color='blue', width=2)))
fig_weekday.add_trace(go.Scatter(x=['Mon', 'Tue', 'Wed', 'Thu','Fri','Sat', 'Sun'], y= [11.340726, 10.077500, 10.738615,7.517533, 9.108171, 9.218644,10.360167  ], name='PM2.5-2021',  mode='lines',line = dict(color='black', width=2)))
fig_weekday.update_layout(title='PM trends during weekdays and weekends', paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig_weekday.update_xaxes(title_text='Day of the Week', showline=True,  linewidth=2, linecolor='black')
fig_weekday.update_yaxes(title_text='Annual Mean PM concentration (μgm-3)', showline=True, linewidth=2, linecolor='black')
#Code for figure 6

pm_annual_mean_19 = df.loc[df['year']==2019].groupby(['hour_of_day']).aggregate('mean')
pm_annual_mean_20 =df.loc[df['year']==2020].groupby(['hour_of_day']).aggregate('mean')
pm_annual_mean_21 =df.loc[df['year']==2021].groupby(['hour_of_day']).aggregate('mean')
pm_annual_mean_21

#line plot shows the change of PM concentration with time 
#concluding remarks from this plot : both PM concentration decreases between 10 am to 
data = [pm_annual_mean_19, pm_annual_mean_20, pm_annual_mean_21]
fig_amean = go.Figure()
fig_amean.add_trace(go.Scatter(x=data[0].index, y= data[0].iloc[:, 2], name='PM10-2019',  mode='lines',line = dict(color='black', width=2)))
fig_amean.add_trace(go.Scatter(x=data[0].index, y= data[0].iloc[:, 3], mode='lines', name='PM2.5-2019',line = dict(color='black', width=2) ))
fig_amean.add_trace(go.Scatter(x=data[1].index, y= data[1].iloc[:, 2], name='PM10-2020',  mode='markers', line = dict(color='black', width=2)))
fig_amean.add_trace(go.Scatter(x=data[1].index, y= data[1].iloc[:, 3], mode='markers', name='PM2.5-2020', line = dict(color='black', width=2)))
#2021
fig_amean.add_trace(go.Scatter(x=data[2].index, y= data[2].iloc[:, 2], name='PM10-2021',  mode='lines+markers', line = dict(color='blue', width=2)))
fig_amean.add_trace(go.Scatter(x=data[2].index, y= data[2].iloc[:, 3], mode='lines+markers', name='PM2.5-2021', line = dict(color='blue', width=2)))

fig_amean.update_xaxes(title_text='Time(hours)', showline=True,  linewidth=2, linecolor='black')
fig_amean.update_yaxes(title_text='Pollutant concentration (μgm-3)', showline=True, linewidth=2, linecolor='black')
fig_amean.update_layout(title='PM2.5 concentration in relation to the annual limit value', paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig_amean.add_hline(y=10, annotation_text="", annotation_position="top left")
fig_amean.add_vrect(x0=10, x1=21, line_width=0, fillcolor="grey", opacity=0.2, annotation_text="drop", annotation_position="top left")
fig_amean.update_layout(legend=dict(
    yanchor="bottom",
    y=0.01,
    xanchor="right",
    x=1.4
))

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
        "Air quality data visualization for AURN Station: London N. Kensington "),
    dbc.Container(
        [dbc.Row(
            [dbc.Col(dcc.Graph(id='graph', figure=figure1), width=6),
            dbc.Col(dcc.Graph(id='graph-1', figure=figure2), width=6)]
        ),
        dbc.Row(
            [dbc.Col(dcc.Graph(id='graph-2', figure=figure3), width=12)]
        ), 
        dbc.Row(
            [dbc.Col(dcc.Graph(id='graph-3', figure=figure4), width=12)]
        ),
        dbc.Row(
            [dbc.Col(dcc.Graph(id='graph-4', figure=fig_weekday), width=6),
            dbc.Col(dcc.Graph(id='graph-5', figure=fig_amean), width=6)]
        )
        ]
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
    ]),
    html.H3("Let's connect on LinkedIn"),
    html.A([
        html.Img(
                src='/assets/linkedin-logo.jpeg',
                style={
                    'height' : '5%',
                    'width' : '5%',
                    'float' : 'center',
                    'position' : 'relative',
                    'padding-top' : 2,
                    'padding-right' : 0
                })
    ], href='https://www.linkedin.com/in/suraiyazabeen/')

])

#Define callback to update graph
@app.callback(
    Output(component_id='graph', component_property='figure'),
    Output(component_id='graph-1', component_property='figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
    figure1 = px.histogram(df, x='AirQuality-PM2.5')
    figure1.update_layout(title='Air quality index histogram for 5 years', paper_bgcolor='rgba(0,0,0,0)',
plot_bgcolor='rgba(0,0,0,0)')
    return figure1, figure2
# -------------------------- MAIN ---------------------------- #


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)