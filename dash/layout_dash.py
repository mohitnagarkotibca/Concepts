# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:26:54 2020

@author: HP
"""
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

data= pd.read_csv('matches.csv')

app= dash.Dash(__name__)

# app.layout= html.Div(
#     dbc.Button(
#         'success',
#         color='success'
#         )
#     )



app.layout= html.Div([
    dbc.Row(
        dbc.Col(html.H3('First Col'),width={'size':'6','offset':3,'order':0})
        #size can be True(It will allocate the entire line) and Auto(It wil automaticall expand till the end of sring)
        # offset(Number of individual columns which are added left to the text)
        #order the manner in which we want to display the components
    ),
    dbc.Row(
        dbc.Col(dcc.Graph(id='pie chart 1',figure={}),
                width=4, lg={'size':6,'offset':0}
                #lg represent large and for larger screen or more the size will be 6 and offset will be 0
                )
        )
    ])

@app
app.run_server(debug=True)







