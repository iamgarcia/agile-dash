from dash import dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import dash
import dash_bootstrap_components as dbc
import requests


dash.register_page(__name__, path='/signup')

alert = html.Div(
    [
        dcc.Store(id='signup_alert_data')
    ],
    id='signup_alert_div',
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

first_name_form = dbc.FormFloating(
    [
        dbc.Input(
            id='fname',
            type='text',
            placeholder='John',
        ),
        dbc.Label('First name'),
    ],
    className='mb-3',
)

last_name_form = dbc.FormFloating(
    [
        dbc.Input(
            id='lname',
            type='text',
            placeholder='Doe',
        ),
        dbc.Label('Last name'),
    ],
    className='mb-3',
)

signup_button = html.Div(
    [
        dbc.Button('Create your Agile Dash account'),
    ],
    id='signup_button',
    className='d-grid',
)

form = dbc.Form(
    [
        email_form,
        password_form,
        first_name_form,
        last_name_form,
        signup_button,
        dcc.Store(id='signup_form_data')
    ],
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4(
                'Let Agile Dash help you be more productive.',
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
    Output('email', 'value'),
    Output('password', 'value'),
    Output('fname', 'value'),
    Output('lname', 'value'),
    Output('signup_form_data', 'data'),
    Input('signup_button', 'n_clicks'),
    State('email', 'value'),
    State('password', 'value'),
    State('fname', 'value'),
    State('lname', 'value'),
)
def store_form_data(n_clicks, email, password, fname, lname):
    if (email is None or password is None or
            fname is None or lname is None):
        raise PreventUpdate

    data = {
        'email': email,
        'password': password,
        'fname': fname,
        'lname': lname
    }

    return '', '', '', '', data


@dash.callback(
    Output('signup_alert_data', 'data'),
    Input('signup_form_data', 'data'),
    prevent_initial_call=True,
)
def send_form_to_server(payload):
    res = requests.post(url='http://127.0.0.1:5000/signup', json=payload)

    return {
        'status_code': res.status_code,
        'message': res.text
    }


@dash.callback(
    Output('signup_alert_div', 'children'),
    Input('signup_alert_data', 'data'),
    State('signup_alert_div', 'children'),
    prevent_initial_call=True,
)
def show_alert(data, alert_div):
    # Delete preexisting alert, if applicable.
    if len(alert_div) == 2:
        alert_div.pop()

    # Apply the proper styling to the alert using status codes.
    if data['status_code'] == 200:
        alert_type = 'success'
    else:
        alert_type = 'danger'

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
