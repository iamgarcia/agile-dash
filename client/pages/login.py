from dash import dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import dash
import dash_bootstrap_components as dbc
import requests


dash.register_page(__name__, path='/login')

alert = html.Div(
    [
        dcc.Store(id='login_alert_data')
    ],
    id='login_alert_div',
)

email_form = dbc.FormFloating(
    [
        dbc.Input(
            id='email',
            type='email',
            placeholder='example@domain.com',
        ),
        dbc.Label('Email address'),
    ],
    className='mb-3',
)

password_form = dbc.FormFloating(
    [
        dbc.Input(
            id='password',
            type='password',
            placeholder='Secret password',
        ),
        dbc.Label('Password'),
    ],
    className='mb-3',
)

login_button = html.Div(
    [
        dbc.Button('Login'),
    ],
    id='login_button',
    className='d-grid',
)

form = dbc.Form(
    [
        email_form,
        password_form,
        login_button,
        dcc.Store(id='login_form_data')
    ],
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4(
                'Log in to your account.',
                className='card-title mb-3',
            ),
            alert,
            form,
        ],
        id='card-body',
    ),
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    card,
                    xs=11,
                    sm=10,
                    md=8,
                    lg=6,
                    xl=5,
                    xxl=4,
                ),
            ],
            justify='center',
        ),
    ]
)


@dash.callback(
    Output('login_form_data', 'data'),
    Input('login_button', 'n_clicks'),
    State('email', 'value'),
    State('password', 'value'),
)
def store_form_data(n_clicks, email, password):
    if (email is None or password is None):
        raise PreventUpdate

    data = {
        'email': email,
        'password': password
    }

    return data


@dash.callback(
    Output('login_alert_data', 'data'),
    Output('session_data', 'data'),
    Input('login_form_data', 'data'),
    prevent_initial_call=True,
)
def send_form_to_server(payload):
    res = requests.post(url='http://127.0.0.1:5000/login', json=payload)

    # Parse json response to a dictionary.
    json_res = res.json()

    # Create lists containing keys to extract
    alert_keys = ['status_code', 'message']
    session_keys = ['session_id', 'user_id']

    # Split response dictionary into two dictionaries.
    alert_data = {
        key: json_res[key]
        for key in alert_keys
        if key in json_res
    }

    session_data = {
        key: json_res[key]
        for key in session_keys
        if key in json_res
    }

    return alert_data, session_data


@dash.callback(
    Output('login_alert_div', 'children'),
    Input('login_alert_data', 'data'),
    State('login_alert_div', 'children'),
    prevent_initial_call=True,
)
def show_alert(data, alert_div):
    # Delete preexisting alert, if applicable.
    if len(alert_div) == 2:
        alert_div.pop()

    # Apply the proper styling to the alert using status codes.
    if data['status_code'] == 400:
        alert_type = 'danger'
    else:
        raise PreventUpdate

    # Create alert component
    alert = dbc.Alert(
        data['message'],
        id='alert-fade',
        color=alert_type,
        dismissable=True,
        is_open=True,
    )

    alert_div.append(alert)
    return alert_div
