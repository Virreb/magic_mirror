import datetime
import numpy as np
import plotly.graph_objs as go


def get_time_graph():

    # Get current time and parse hours, minutes, seconds
    datetime_string = datetime.datetime.now().__str__()
    time_string = datetime_string.split(' ')[1].split('.')[0]
    date_string = datetime_string.split(' ')[0]
    time_arr = time_string.split(':')
    hour = float(time_arr[0])%12
    minute = float(time_arr[1])
    second = float(time_arr[2])

    # Convert to clock angles
    radius = 90
    hour_angle = hour/6*np.pi + np.pi/6*minute/60
    min_angle = minute/30*np.pi + np.pi/30*second/60

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
            xaxis=dict(range=[-100, 100],
                       showgrid=False,
                       zeroline=False,
                       showline=False,
                       autotick=False,
                       ticks='',
                       showticklabels=False),

            yaxis=dict(range=[-100, 100],
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
