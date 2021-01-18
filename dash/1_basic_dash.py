# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 02:31:06 2020

@author: HP
"""
#imports-------------------------
import dash 
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
# data-----------------------------
# df = pd.DataFrame({
#     'Target_time':[90,90,120,60,120,90,60,120,60,120,120,120,120,120,120,120],
#     'studied_time':[39,13,110,50,120,70,40,10,50,30,70,50,120,20,20,60,],
#     'took_sleep': ['no','no','yes','yes','yes','no','no','no','yes','yes','no','no','no','no','no','no']
#     })
# df_group= df.groupby('took_sleep')['studied_time'].mean()

#---
data= pd.read_csv('most_runs_average_strikerate.csv')
data.columns
top_10= data.sort_values(by='total_runs',ascending=False)[:10]

#Visualization-------------------------------

# fig= go.Figure(
#     go.Bar(
#         x=df_group.index,
#         y=df_group.values
#         ),
#     layout={
#         'xaxis_title':'slept?',
#         'yaxis_title':'Average time studied'
#         }    
#     )

#---
# fig= go.Figure(
#     go.Scatter(
#         x= data['average'].values,
#         y= data['strikerate'].values,
#         text= data['batsman'].values,
#         marker={'size':data['total_runs'].values / 100},
#         mode='markers'
#         ),
#     layout={
#         'xaxis_title':'Average',
#         'yaxis_title':'strike rate',
#         'title':' Comparision of average and strike rate'        
#         }
#     )

# fig.add_annotation(
#     x= 37.711864406779654,
#     y= 138.80224578914536,
#     showarrow= True,
#     ax= 20,
#     ay=90,
#     text='Dhoni'
#     )


#app--------------------------------
app= dash.Dash(__name__)
app.layout = html.Div(
    children= [
        html.H1(' Does Average affects stike rate ?'),
        html.Br(),
        html.Div(['Input: ', dcc.Input(id='input',
                                      value ='Initial_value',
                                      type='text')]),
        html.Br(),
                html.Div(['Input: ', dcc.Input(id='input2',
                                      value ='enter a number',
                                      type='text')]),

        html.Br(),
        html.Div(id='output1'),
        html.Br(),
        html.Div(id='output2')
        ]
    )
@app.callback(
    Output(component_id='output1',component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

@app.callback(
    Output(component_id='output2',component_property='children'),
    [Input(component_id='input2',component_property='value')]
    )
def update_output_2(val):
    return int(val)**2


if __name__== '__main__':
    app.run_server(debug=False)