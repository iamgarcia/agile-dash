from dash import dcc, Dash, html, Input, Output, State
import dash
import dash_bootstrap_components as dbc


app = Dash(__name__,
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

# Branding component
brand = html.Div(
    dbc.Row(
        [
            dbc.Col(html.Img(src='assets/agile-logo.png', height='30px')),
            dbc.Col(dbc.NavbarBrand('Agile Dash', className='ms-2')),
        ],
        align='center',
        className='g-0',
    ),
)

# Account component
account = html.Div(
    [
        dbc.Button(
            'Log in',
            href=dash.page_registry['pages.login']['relative_path'],
            color='primary',
            className='ms-2',
            n_clicks=0,
        ),
        dbc.Button(
            'Sign up',
            href=dash.page_registry['pages.signup']['relative_path'],
            outline=True,
            color='light',
            className='ms-2',
            n_clicks=0,
        ),
    ],
    className='d-grid gap-2 d-md-block',
)

# Navigation contents component
nav_contents = [
    dbc.NavItem(
        dbc.NavLink(
            dash.page_registry['pages.dashboard']['name'],
            href=dash.page_registry['pages.dashboard']['relative_path'],
        )
    ),
    dbc.NavItem(
        dbc.NavLink(
            dash.page_registry['pages.board']['name'],
            href=dash.page_registry['pages.board']['relative_path'],
        )
    ),
    dbc.NavItem(
        dbc.NavLink(
            dash.page_registry['pages.reports']['name'],
            href=dash.page_registry['pages.reports']['relative_path'],
        )
    ),
    account,
]

# Navigation component
nav = dbc.Nav(
    nav_contents,
    justified=True,
    className='ms-auto',
    navbar=True,
)

# Navigation bar component
navbar = dbc.Navbar(
    dbc.Container(
        [
            brand,
            dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),
            dbc.Collapse(
                nav,
                id='navbar-collapse',
                navbar=True,
            ),
        ],
    ),
    color='dark',
    dark=True,
    className='mb-5',
)

# Main application layout
app.layout = html.Div(
    [
        navbar,
        dash.page_container,
        dcc.Store(id='session_data', storage_type='session'),
    ]
)


# Callback for toggling the collapse on small screens
@app.callback(
    Output('navbar-collapse', 'is_open'),
    [Input('navbar-toggler', 'n_clicks')],
    [State('navbar-collapse', 'is_open')],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)  # Hot-reloading enabled
