# -*- coding : utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash !'),

    html.Div(children='''
    Dash : a web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data' : [
                {'x' : [1, 2, 3], 'y' : [4, 2, 3], 'type' : 'bar', 'name' : 'SF'},
                {'x' : [1, 2, 3], 'y' : [6, 4, 1], 'type' : 'bar', 'name' : 'Montréal'}
            ],
            'layout' : {
                'title' : 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)