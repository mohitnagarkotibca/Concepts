# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:52:11 2020

@author: HP
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input,Output
import base64
import dash_bootstrap_components as dbc

app= dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

image= base64.b64encode(open('1.jpg','rb').read())

card_one= dbc.Card([
    dbc.CardImg(src='data:image/png;base64,{}'.format(image.decode()),top=True, bottom=False,alt='Not working'),
    dbc.CardBody([
        html.H6('Batman is Awsome',className='card-title'),
        dbc.Button('Press Me',href='http://google.com',target='_blank',color='success')]
        )],outline=True
    )

image2= base64.b64encode(open('2.jpg','rb').read())
card_two= dbc.Card([
    dbc.CardImg(src='data:image/png;base64,{}'.format(image2.decode()),top=True, bottom=False,alt='Not working'),
    dbc.CardBody([
        html.H6('Batman is Awsome',className='card-title'),
        dbc.Button('Press Me',href='http://google.com',target='_blank',color='success')]
        )],outline=True
    )

app.layout = html.Div(children=[
    dbc.Row(
        [
            dbc.Col(card_one),
            dbc.Col(card_two),
            dbc.Col(card_two)
        ]
        ),
        dbc.Row(
        [
            dbc.Col(card_one),
            dbc.Col(card_two),
            dbc.Col(card_two)
        ]
        ) 
]
)
app.run_server(debug=True)

