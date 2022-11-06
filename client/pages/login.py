from dash import dcc, html, Input, Output, State
import dash
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/login')

layout = dbc.Container(
    [
        html.H1('This is the log in page')
    ]
)