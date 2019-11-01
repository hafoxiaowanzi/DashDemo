
from flask import Flask, flash, render_template, request, session
import os, dash
import dash_html_components as html
import dash_core_components as dcc
import flask

app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash_app/')
dash_app.config['suppress_callback_exceptions']=True

def index_page():
    index = html.Div([
        dcc.Link('Page 1', href='/page1'),
        html.Br(),
        dcc.Link('Page 2', href='/page2'),
        html.Br(),
        dcc.Link('Page 3', href='/page3'),
        html.Br()
    ])
    return index

dash_app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id = 'page-content')
])

page_1 = html.Div([
    html.H1('Welcome to page 1'),
    index_page()
])

page_2 = html.Div([
    html.H1('Welcome to page 2'),
    index_page()
])

page_3 = html.Div([
    html.H1('Welcome to page 3'),
    index_page()
])

@dash_app.callback(
    dash.dependencies.Output('page-content','children'),
    [dash.dependencies.Input('url','pathname')]
)
def display_page(pathname):
    if pathname == '/page1':
        return page_1
    if pathname == '/page2':
        return page_2
    if pathname == '/page3':
        return page_3
    else:
        return index_page()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return flask.redirect('/dash_app')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=5000)