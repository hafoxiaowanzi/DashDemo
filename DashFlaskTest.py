import numpy as np
import pandas as pd 
from sklearn import datasets
import plotly.figure_factory as ff

from flask import Flask

import dash
import dash_core_components as dcc
import dash_html_components as html


server = Flask(__name__)



# app1.layout = html.Div([
#     html.Div(
#         children =[html.H1(children ='趋势 1'),]
#     )
#     ])

iris=datasets.load_iris()
data = pd.DataFrame(iris.data, columns=['SpealLength', 'Spealwidth',
                                        'PetalLength', 'PetalLength'])
data = data[:30]


# @server.route('/test1')
# def do_test1():
#     return test(app1,data)

# @server.route('/test2')
# def do_test2():
#     return test2(app1,data)

# @server.route('/test3')
# def do_test3():
#     return test3(app1,data) 

# @server.route('/test4')
# def do_test4():
#     return test4(app1,data)

# @server.route('/test5')
# def do_test5():
#     return test5(app1,data)

@server.route('/')
def do_main():
    app1 = dash.Dash(__name__,server=server,url_base_pathname='/')
    test6(app1,data)
    return  


def test(app, data):
    y = np.array(data['SpealLength'])
    x = range(len(y))
    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='line',
            figure={
                'data': [
                    {'x': x, 'y': y, 'type': 'Scatter', 'name': 'Line'},
                ],
                'layout': {
                    'title': '线图'
                }
            }
        )
    ])
def test2(app, data):
    y = np.array(data['PetalLength'])
    x = range(len(y))
    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='bar',
            figure={
                'data': [
                    {'x': x, 'y': y, 'type': 'bar', 'name': 'Bar'},
                ],
                'layout': {
                    'title': '柱图'
                }
            }
        )
    ])
def test3(app, data):
    y = np.array(data['SpealLength'])
    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='hist',
            figure={
                'data': [
                    dict(
                        type='histogram', x=y, name='Hist'
                    )
                ],
                'layout': {
                    'title': '直方图'
                }
            }
        )
    ])


def test4(app, data):
    data['group1'] = data['SpealLength'].apply(lambda x: int(x * 4) / 4.0)
    x = data['group1'] # 按length分类，统计width
    y = np.array(data['Spealwidth'])
    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='box',
            figure={
                'data': [
                    dict(
                        type='box', x=x, y=y, name='Box'
                    )
                ],
                'layout': {
                    'title': '箱图'
                }
            }
        )
    ])
def test5(app, data):    
    data['group1'] = data['SpealLength'].apply(lambda x: int(x))
    tmp = data.groupby('group1').size().to_frame()
    tmp = tmp.rename(columns={0: 'num'})
    tmp = np.round(tmp, 4).reset_index(drop=False)

    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='pie',
            figure={
              'data': [
                    dict(
                        type='pie', name='Pie',
                        labels=tmp['group1'].tolist(),
                        values=tmp['num'].tolist(),
                    )                  
                ],
                'layout': {
                    'title': '饼图'
                }
            }
        )
    ])

def test6(app, data):
    table = ff.create_table(data.head()) 
    for i in range(len(table.layout.annotations)):
        table.layout.annotations[i].font.size = 15
    app.layout = html.Div(children=[
        html.H1(children='Demo'),
        dcc.Graph(
            id='table',
            figure=table
        )
    ])
if __name__ =='__main__':
    server.run(debug=True,port=8051,host="0.0.0.0")