import dash
import dash_core_components as dcc
import dash_html_components as html
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

def filter_dropdown(dropdown_value):
    return df.loc[ df[df.columns[0]] == dropdown_value, df.columns[4] ].dropna().unique()

app.layout = html.Div([
    html.H6('Tenrikyology Content Search'),
    html.Hr(),
    dropdown(df.columns[0]),
    html.Br(),
    ddc.Dropdown(id=df.columns[1])
])

@app.callback(
    Output(component_id=df.columns[1], component_property='children'),
    [Input(component_id=df.columns[0], component_property='value')]
)

if __name__ == '__main__':
    app.run_server(debug=True)