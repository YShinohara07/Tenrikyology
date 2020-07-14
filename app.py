import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('TenrikyologyContent.csv')
font_style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=font_style)



if __name__ == '__main__':
    app.run_server(debug=True)