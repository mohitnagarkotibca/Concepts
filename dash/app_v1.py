# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 02:07:08 2020

@author: HP
"""
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import punkt
from nltk.corpus.reader import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import re
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#7ab472',
    'text': '#fad0bb',
    'header_table': '#9cd49e'
}

markdown_text1 = '''

This application gathers the latest news from the newspapers **The Hindu**, **The Asian Age**,**'Hindustan Times'** and **The Mint**, predicts their category between **Politics**, **Business**, **Entertainment**, **Sport**, **Tech** and **Other** and then shows a graphic summary.

The news categories are predicted with a Support Vector Machine model.

Please enter which newspapers would you like to scrape news off and press **Submit**:

'''
markdown_text2 = '''

The scraped news are converted into a numeric feature vector with TF-IDF vectorization. Then, a Support Vector Classifier is applied to predict each category.

'''

app.layout = html.Div(style={'backgroundColor':colors['background']}, children=[
    
    # Title
    html.U(html.B(
    html.H1(children='News Classification App',
            style={
                'textAlign': 'center',
                'padding': '20px',
                'backgroundColor':'#27ae60'
            },
            className='banner',
           ))),

    # Sub-title Left
    html.Div([
        dcc.Markdown(children=markdown_text1)],
        style={'width': '49%', 'display': 'inline-block'}),
    
    # Sub-title Right
    html.Div([
        dcc.Markdown(children=markdown_text2)],
        style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),

    # Space between text and dropdown
    html.H1(id='space', children=' '),

    # Dropdown
    html.Div([
        dcc.Dropdown(
            options=[
                {'label': 'The hindu', 'value': 'TH'},
                {'label': 'Hindustan Times', 'value': 'HT'},
                {'label': 'The Asian Age', 'value': 'TAA'},
                {'label': 'The Mint', 'value': 'TM'}
                
            ],
            value=['TH', 'TAA'],
            multi=True,
            id='checklist')],
        style={'width': '95%', 'display': 'inline-block', 'float': 'left'}),
        

    # Button
    html.Div([
        html.Button('Submit', id='submit', type='submit')],
        style={'float': 'center'}),
    
    # Output Block
    html.Div(id='output-container-button', children=' '),
    
    # Graph1
    html.Div([
        dcc.Graph(id='graph1')],
        style={'width': '49%', 'display': 'inline-block'}),
    
    # Graph2
    html.Div([
        dcc.Graph(id='graph2')],
        style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    
    # Table title
    html.Div(id='table-title', children='You can see a summary of the news articles below:'),

    # Space
    html.H1(id='space2', children=' '),
    
    # # Table
    # html.Div([
    #     dash_table.DataTable(
    #         id='table',
    #         columns=[{"name": i, "id": i} for i in ['Article Title', 'Article Link', 'Newspaper', 'Prediction']],
    #         style_data={'whiteSpace': 'normal'},
    #         style_as_list_view=True,
    #         style_cell={'padding': '5px', 'textAlign': 'left', 'backgroundColor': colors['background']},
    #         style_header={
    #             'backgroundColor': colors ['header_table'],
    #             'fontWeight': 'bold'
    #         },
    #         style_table={
    #             'maxHeight': '300',
    #             'overflowY':'scroll'
                
    #         },
    #         css=[{
    #             'selector': '.dash-cell div.dash-cell-value',
    #             'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
    #         }]
    #     )],
    #     style={'width': '75%','float': 'left', 'position': 'relative', 'left': '12.5%', 'display': 'inline-block'}),    
        
    # Hidden div inside the app that stores the intermediate value
    html.Div(id='intermediate-value', style={'display': 'none'})
    

])

app.run_server(debug= True)
