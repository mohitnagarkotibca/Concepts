# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:41:19 2020

@author: HP
"""

import dash
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import dash_html_components as html
import plotly.graph_objects as go
import re 


                    
app= dash.Dash(__name__)
#Data Feeding-------------------------

data=pd.read_csv('matches.csv')
def rep(team):
    if team == 'Deccan Chargers':
        return 'Sunrisers Hyderabad'
    elif team =='Delhi Daredevils':
        return 'Delhi Capitals'
    else:
        return team
    
data['winner']= data['winner'].apply(rep)
teams= data['winner'].value_counts().index[:8]
data_g= data.groupby('Season').get_group('IPL-2018')['winner'].value_counts()

fig= go.Figure(
                go.Bar(
                    x= teams,
                    y= data_g[teams].values
                    )
    )

#Layout-------------------------------
app.layout= html.Div(
    children=[
        html.Br(),
        html.Br(),
        html.Div(
            dcc.Slider(
                id='input_slider',
                min=2008,
                max=2019,
                step= 0.01,
                value=2008,
                updatemode='drag'
                ),
            style={'width':'40%'}
            ),
        html.Div(id='output_year')
            ,
        html.Div(
        dcc.Graph(
            id='output_graph',
            figure=fig
            )
        )
        ]
    )


#callback-----------------------------
@app.callback(
    [
     Output(component_id='output_graph',component_property='figure'),
     Output(component_id='output_year',component_property='children')
    ],
    [Input(component_id='input_slider',component_property='value')]
    )

def output_method(val):
    round_val= round(val)
    data_g= data.groupby('Season').get_group('IPL-{}'.format(round_val))['winner'].value_counts()
    fig= go.Figure(
                    go.Bar(
                        x= teams,
                        y= data_g[teams].values
                        )
        )
    return fig,round_val


app.run_server(debug=False)









