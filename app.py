import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('TenrikyologyContent.csv')
font_style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=font_style)

def dropdown(column, df=df):
    '''Creates dropdown search using string column of dataframe'''
    option = [dict(label=i,value=i) for i in df[column].dropna().unique()]
    return html.Div([
        html.Label(column),
        dcc.Dropdown(options=option, value=column)
    ])


app.layout = dropdown(df.columns[0])


if __name__ == '__main__':
    app.run_server(debug=True)