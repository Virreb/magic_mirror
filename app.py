# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})  # standard style
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})  # grayed out while loading

# GLOBALS
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1920
DEFAULT_BACKGROUND_COLOR = 'black'
DEFAULT_COLOR = 'white'

app.layout = html.Div(  # MAIN DIV
    style={
        'color': DEFAULT_COLOR,
        'width': f'{SCREEN_WIDTH}px',
        'height': f'{SCREEN_HEIGHT}px',
        'backgroundColor': DEFAULT_BACKGROUND_COLOR
    },
    children=[

        # This is a test output div
        html.Div(
            style=
            {
                'position': 'absolute',
                'left': '50px',
                'top': '50px',
            },
            children=[
                html.H1(id='test-h1', children='Test Div'),
                html.H2(id='test-h2')
            ]
        ),
        # This is a test input div
        html.Div(
            style={
                'position': 'absolute',
                'left': f'{SCREEN_WIDTH - 300}px',
                'top': '50px'
            },
            children=[
                html.Label('This is a test input'),
                dcc.Input(id='test-input', type='text', placeholder='Input text', value='temp'),

                html.Br(),

                html.Button('Calculate!', n_clicks=0, id='test_button', className='button-primary'),
            ]
        )
    ]
)


@app.callback(  # callback to get parameters and show result
    Output('test-h1', 'children'),
    [Input('test_button', 'n_clicks')],   # fire state when submit button is pressed
    [State('test-input', 'value'),
     ]
)
def get_output(submit_button_clicks: int, test_input: str):

    #if submit_button_clicks > 0:
    return f'{submit_button_clicks}, {test_input}'

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
