import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chrisddyp/pen/bWLwgsP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#text = 'dash sucksss ;P'
#app.layout = html.Div(children=[html.H1(children='welcome jerry'),html.Div(children=text)]
app.layout = html.Div([html.H5(children='Category / Sub-category Toggle Switch'), daq.BooleanSwitch(id = "boolean-switch", on=True, color="Pink"), dcc.Graph(id='pie-chart')])
df=pd.read_csv('calc_summary.csv')
@app.callback(dash.dependencies.Output('pie-chart','figure'),[dash.dependencies.Input('boolean-switch','on')])
def update_output(switch_status):
    grouping_field= 'Lineup'
    if switch_status == False:
        grouping_field='Date'
    fig = px.pie(df, values='Amount', names=grouping_field)
    fig_title= 'Revenue by ' + grouping_field
    fig.update_layout(title_text = fig_title)
    return 'The switch is {}.'.fomrat(switch_status)

if __name__ == '__main__':
    app.run_server(debug=True)

