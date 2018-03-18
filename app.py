# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import clock
import vasttrafik_info
import json
import os

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
else:
    print('ERROR! Need config.json file for loading parameters, aborting.')
    exit(0)


app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})  # standard style
# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})  # grayed out while loading

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

        # Show busstimes from Västtrafik
        html.Div(
            style=
            {
                'position': 'absolute',
                'left': '50px',
                'top': '50px',
            },
            children=[
                html.Div(id='vasttrafik-table'),
                dcc.Interval(
                    id='vasttrafik-interval',
                    interval=60*1000,  # 60 seconds in milliseconds
                    n_intervals=0
                )
                ]
        ),

        # Show clock
        html.Div(
            style=
            {
                'position': 'absolute',
                'left': f'{SCREEN_WIDTH - 500}px',
                'top': '50px',
            },
            children=[
            dcc.Graph(id='live-update-clock'),
            dcc.Interval(
                id='clock-interval',
                interval=1*1000,    # in milliseconds
                n_intervals=0
            )
        ]),
    ]
)


@app.callback(Output('live-update-clock', 'figure'),     # Update clock every second
              [Input('clock-interval', 'n_intervals')])
def update_clock_time(n):
    return clock.get_time_graph()


@app.callback(Output('vasttrafik-table', 'children'),     # Update buss table every minute
              [Input('vasttrafik-interval', 'n_intervals')])
def update_vasttrafik_table(n):
    return vasttrafik_info.VTInfo(**config['vasttrafik']).display_info()

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
