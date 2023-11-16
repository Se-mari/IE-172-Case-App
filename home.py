# Usual Dash dependencies
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import dash
from dash.exceptions import PreventUpdate
import pandas as pd
# Let us import the app object in case we need to define
# callbacks here
from app import app

# store the layout objects into a variable named layout
layout = html.Div(
        [
            html.H2('Welcome to our app!'),
            html.Hr(),
            html.Div(
                [
                    html.Span(
                        "Thru this app, you can manage a database of movies that are classified according to genres.",
                    ),
                    html.Br(),
                    html.Br(),
                    html.Span(
                        "Contact the owner if you need assistance!",
                        style={'font-style':'italic'}
                    ),
                ]
                )
            ]
        )
