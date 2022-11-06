from dash import dcc, html, Input, Output, State
import dash
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/signup')

email_form = dbc.FormFloating(
    [
        dbc.Input(type='email', placeholder='example@domain.com'),
        dbc.Label('Email address'),
    ],
    className='mb-3',
)

password_form = dbc.FormFloating(
    [
        dbc.Input(
            type='password',
            placeholder='Secret password',
        ),
        dbc.Label('Password'),
    ],
    className='mb-3',
)

first_name_form = dbc.FormFloating(
    [
        dbc.Input(type='text', placeholder='John'),
        dbc.Label('First Name'),
    ],
    className='mb-3',
)

last_name_form = dbc.FormFloating(
    [
        dbc.Input(type='text', placeholder='Doe'),
        dbc.Label('Last Name'),
    ],
    className='mb-3',
)

layout = dbc.Container(
    [
        html.H2('Lorem ipsum dolor sit amet consectetur.'),
        email_form,
        password_form,
        first_name_form,
        last_name_form,
        dbc.Button('Sign up'),
    ]
)