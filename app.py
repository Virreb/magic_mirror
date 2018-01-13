# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import time
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        html.Div(id='live-update-text'),
        html.Div(id='live-update-time'),
        html.Div(id='live-update-date'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)



@app.callback(Output('live-update-time', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    time_string = time.strftime("%H:%M:%S", time.gmtime())
    return [
        html.Span(time_string)
    ]


@app.callback(Output('live-update-date', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    date_string = time.strftime("%Y-%m-%d", time.gmtime())
    return [
        html.Span(date_string)
    ]


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):

    traces = list()

    traces.append(go.Scatter(
        x=0,
        y=0
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'range': [-100, 100]},
            yaxis={'range': [-100, 100]},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
