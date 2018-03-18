# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import clock

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-update-clock'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-clock', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    clock.update_time()

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
