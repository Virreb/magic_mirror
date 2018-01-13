# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import vasttrafik_info

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(vasttrafik_info.VTInfo('Brunnsparken', ['sname', 'time', 'rtTime', 'direction']).display_info())
])

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
