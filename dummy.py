import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Hello World")
])

if __name__ == "__main__":
    app.run_server(debug=True)

