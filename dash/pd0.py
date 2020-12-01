# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:30:07 2020

@author: HP
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app= dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


# popover = html.Div(
#     [
#         dbc.Button(
#             "Click to toggle popover", id="popover-target", color="danger"
#         ),
#         dbc.Popover(
#             [
#                 dbc.PopoverHeader("Popover header"),
#                 dbc.PopoverBody("And here's some amazing content. Cool!"),
#             ],
#             id="popover",
#             is_open=False,
#             target="popover-target",
#         ),
#     ]
# )

# app.layout=html.Div(
#     [
#      popover
#      ])
# @app.callback(
#     Output("popover", "is_open"),
#     [Input("popover-target", "n_clicks")],
#     [State("popover", "is_open")],
# )
# def toggle_popover(n, is_open):
#     if n:
#         return not is_open
#     return is_open
#--------------------------------------------------------------------


# def make_popover(placement):
#     return dbc.Popover(
#         [
#             dbc.PopoverHeader("Header"),
#             dbc.PopoverBody(f"This is a {placement} popover"),
#         ],
#         id=f"popover-{placement}",
#         target=f"popover-{placement}-target",
#         placement=placement,
#     )


# def make_button(placement):
#     return dbc.Button(
#         f"Popover on {placement}",
#         id=f"popover-{placement}-target",
#         className="mx-2",
#     )


# popovers = html.Div(
#     [make_button(p) for p in ["top", "left", "right", "bottom"]]
#     + [make_popover(p) for p in ["top", "left", "right", "bottom"]]
# )


# def toggle_popover(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# for p in ["top", "left", "right", "bottom"]:
#     app.callback(
#         Output(f"popover-{p}", "is_open"),
#         [Input(f"popover-{p}-target", "n_clicks")],
#         [State(f"popover-{p}", "is_open")],
#     )(toggle_popover)

# app.layout=html.Div(
#     [
#       popovers
#       ])

def make_button(i):
    button= dbc.Button(
        'button_'+str(i),
        id= 'button_'+str(i)
        )
    return button

def make_popover(i):
    popover= dbc.Popover(
        [
        dbc.PopoverHeader('button_{}_header'.format(str(i))),
        dbc.PopoverBody('button_{}_body'.format(str(i)))
        ],
                        
        id='popover_id_{}'.format(str(i)),
        target= 'button_{}'.format(str(i))
        )
    return popover

popovers= html.Div([make_button(i) for i in range(10)]+[make_popover(i) for i in range(10)])


def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

for p in range(10):
    app.callback(
        Output(f"popover_id_{p}", "is_open"),
        [Input(f"button_{p}", "n_clicks")],
        [State(f"popover_id_{p}", "is_open")],
    )(toggle_popover)
    
app.layout=html.Div([
popovers
    ])

app.run_server(debug=False)



