# -*- coding : utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash !',
            style={
            'textAlign': 'center',
            'color': colors['text']
            }),

        html.Div(
            children='''
            Dash : a web application framework for Python.
            ''',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

        dcc.Graph(
            id='example-graph',
            figure={
                'data' : [
                    {'x' : [1, 2, 3], 'y' : [4, 2, 3], 'type' : 'bar', 'name' : 'SF'},
                    {'x' : [1, 2, 3], 'y' : [6, 4, 1], 'type' : 'bar', 'name' : 'Montréal'}
                ],
                'layout' : {
                    'title' : 'Dash Data Visualization',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {'color': colors['text']}
                    }
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)