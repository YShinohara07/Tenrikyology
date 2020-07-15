import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('TenrikyologyContent.csv')
font_style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=font_style)

def dropdown(column):
    '''Creates dropdown search using string column of dataframe'''
    option = [dict(label=i,value=i) for i in df[column].dropna().unique()]
    return html.Div([
        html.Label(column),
        dcc.Dropdown(id=column, options=option, value=column)
    ])

def filter_dropdown(dropdown_str):
    return df.loc[ df[df.columns[0]] == dropdown_str, df.columns[4] ].dropna().unique()

app.layout = html.Div([
    html.H6('Tenrikyology Content Search'),
    html.Hr(),
    dropdown(df.columns[0]),
    html.Br(),
    html.Div([html.Label(df.columns[4]), dcc.Dropdown(id=df.columns[4])]),
    html.Hr(),
    html.Div(id='display_text')
])

@app.callback(
    Output(component_id=df.columns[4], component_property='options'),
    [Input(component_id=df.columns[0], component_property='value')]
)
def filter2nd_column(cat):
    return [{'label':i,'value': i} for i in filter_dropdown(cat)]

@app.callback(
    Output('display_text', 'children'),
    [Input(df.columns[0], 'value'), Input(df.columns[4],'value')]
)
def display_content(cat, title):
    return df.loc[ (df[df.columns[0]]==cat) & (df[df.columns[4]]==title), df.columns[1]]

if __name__ == '__main__':
    app.run_server(debug=True)