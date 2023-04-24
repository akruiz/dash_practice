import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

app=dash.Dash(__name__)

app.layout = html.Div([html.H5(children='wich desert do u want?'), dcc.Dropdown(id='demo-dropdown', options=[{'label':'Cheesecake','value':'cheesecake'},{'label':'Choco','value':'choco'}, {'label':'Ice','value':'ice'}],
                                                                                                                     multi=True, value='cheesecake'), html.Br(), html.Br(), html.Br(), html.Div(id='dd-output-container')]
                      ,className='three columns',style={'padding':50})
#df=pd.read_csv('calc_summary.csv')
@app.callback(dash.dependencies.Output('dd-output-container','children'),[dash.dependencies.Input('demo-dropdown','value')])
def update_output(value):
    return 'you have chosen "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)