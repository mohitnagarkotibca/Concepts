# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:57:04 2020

@author: HP
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
app = dash.Dash(__name__)
#data-----------------------------------------
data= pd.read_csv('matches.csv')
data_g= data.groupby('Season').get_group('IPL-2008')['winner'].value_counts()
#layout---------------------------------------
# fig= go.Figure(
#     go.Scatter(
#         x= data_g.index,
#         y= data_g.values,
#         mode='markers',
#         text= data_g.index,
#         textposition='top right'
#         )
#     )

# for i in range(len(data_g .values)):    
#     fig.add_annotation(
#         x= data_g.index[i],
#         y= data_g.values[i] +20,
#         text= str(data_g.values[i])
#         )

app.layout = html.Div(
              children=[
                  html.H1('Kindly select the Season'),
                  html.Br(),
                  dcc.Dropdown(
                      id='season_select',
                      options=[
                          {'label':'2008','value':'IPL-2008'},
                          {'label':'2009','value':'IPL-2009'},
                          {'label':'2010','value':'IPL-2010'},
                          {'label':'2011','value':'IPL-2011'},
                          {'label':'2012','value':'IPL-2012'},
                          {'label':'2013','value':'IPL-2013'},
                          {'label':'2014','value':'IPL-2014'},
                          {'label':'2015','value':'IPL-2015'},
                          {'label':'2016','value':'IPL-2016'},
                          {'label':'2017','value':'IPL-2017'},
                          {'label':'2018','value':'IPL-2018'},
                          {'label':'2019','value':'IPL-2019'} 
                          ],
                      value='IPL-2008'
                      ),
                  
                  html.Div(
                  dcc.Loading(dcc.Graph(id='output', figure= [])  )                   
                  ,
                  style={'width': '90%'})
                  
                  ]
    )

@app.callback(
             Output(component_id='output',component_property='figure'),
             [Input(component_id='season_select',component_property='value')]
    )
def display_method(val):
    data_g= data.groupby('Season').get_group(val)['winner'].value_counts()
    
    fig= go.Figure(
        go.Scatter( 
            x= data_g.index,
            y= data_g.values,
            mode='markers',
            text= data_g.index,
            textposition='top left'
            )
        )

    for i in range(len(data_g .values)):    
        fig.add_annotation(
            x= data_g.index[i],
            y= data_g.values[i] +1,
            text= str(data_g.values[i]),
            showarrow=False
            )
    return fig
    
    


app.run_server(debug=False)
