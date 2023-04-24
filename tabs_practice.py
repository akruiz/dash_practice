import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chrisddyp/pen/bWLwgsP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([dcc.Tabs(id='tabs-example', value='tab-1', children=[dcc.Tab(label='Tab One', value='tab-1'),
dcc.Tab(label='Tab Two', value='tab-2'),dcc.Tab(label='Tab Three', value='tab-3'),]),html.Div(id='tabs-example-content')])
@app.callback(dash.dependencies.Output('tabs-example-content','children'),[dash.dependencies.Input('tabs-example','value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([html.H3('Welcome to Tab 1!!!')])
    elif tab == 'tab-2':
        return html.Div([html.H3('Welcome to Tab 2!!!')])
    elif tab == 'tab-3':
        return html.Div([html.H3('Welcome to Tab 3!!!')])

if __name__ == '__main__':
    app.run_server(debug=True)