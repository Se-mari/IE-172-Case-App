import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.exceptions import PreventUpdate

from app import app

navlink_style = {
    'color': '#fff'
}

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                dbc.Col(dbc.NavbarBrand("IE 172 Case App", className="ms-2")),
                ],
                align="center",
                className = 'g-0'
            ),
            href="/home",
        ),
        dbc.NavLink("Home", href="/home", style=navlink_style),
        dbc.NavLink("Movies", href="/movies", style=navlink_style),
        dbc.NavLink("Genres", href="/genres", style=navlink_style),
    ],
    color = 'dark',
    dark = True

)