# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import time
import datetime
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)





@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    datetime_string = datetime.datetime.now().__str__()
    time_string = datetime_string.split(' ')[1].split('.')[0]
    date_string = datetime_string.split(' ')[0]
    time_arr = time_string.split(':')
    hour = int(time_arr[0])%12
    minute = int(time_arr[1])
    radius = 90
    hour_angle = float(hour)/6*np.pi
    min_angle = float(minute)/30*np.pi
    traces = list()
    for i in range(12):
        angle = np.pi/6*i
        traces.append(go.Scatter(
            x=[radius * np.sin(angle)],
            y=[radius * np.cos(angle)],
            marker=dict(
                size=10,
                color='rgb(255, 255, 255)',
            )))
    traces.append(go.Scatter(
        x=[radius*np.sin(hour_angle)],
        y=[radius*np.cos(hour_angle)],
        marker=dict(
            size=30,
            color='rgb(255, 165, 0)',
        )))
    traces.append(go.Scatter(
        x=[radius * np.sin(min_angle)],
        y=[radius * np.cos(min_angle)],
        marker=dict(
            size=20,
            color='rgb(0, 191, 255)',
        )))
    traces.append(go.Scatter(
        x=[0, 0],
        y=[-5, 15],
        mode='text',
        name='Text',
        text=[time_string, date_string],
        textposition='bottom'
    ))

    return {
        'data': traces,
        'layout': go.Layout(
            font=dict(family='Courier New, monospace', size=32, color='#ffffff'),
            showlegend=False,
            width=500,
            height=500,
            xaxis=dict(range = [-100, 100],
                       showgrid=False,
                       zeroline=False,
                       showline=False,
                       autotick=False,
                       ticks='',
                       showticklabels=False),
            yaxis=dict(range = [-100, 100],
                       showgrid=False,
                       zeroline=False,
                       showline=False,
                       autotick=False,
                       ticks='',
                       showticklabels=False),
            paper_bgcolor='#000000',
            plot_bgcolor='#000000'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
