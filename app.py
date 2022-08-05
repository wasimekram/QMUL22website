from flask import Flask, render_template, request
#from sqlalchemy import false, true
from scripts.twolink import twolink
import glob
import os
import pandas as pd
import json
import plotly
import plotly.express as px#
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__, static_url_path='/static')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route('/', methods = ['GET', 'POST'])
def index():
    #code for carousel    
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir + os.sep + "static" + os.sep + "images" + os.sep + "results" + os.sep)
    imgs = glob.glob(results_dir + "/*.png")
    df = pd.DataFrame({'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],  'Amount': [4, 1, 2, 2, 4, 5], 'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})   
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')   
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    N=100
    random_x = np.linspace(0, 5, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5
    fig = go.Figure()
    # Add traces
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines+markers',
                    name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='markers',
                    name='markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='lines',
                    name='lines'))
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    if request.method == 'GET':
        return render_template('main.html', imgs=imgs, graphJSON=graphJSON, graphJSON1=graphJSON1)
    if request.method == 'POST':
        armfirst = request.form.get('armfirst')
        data = request.form.to_dict()
        print(data)
        try:
            twolink(data)
            return render_template('main.html', test=data, imgs=imgs)
        except Exception as e: 
            print(e)
            twolink({'armfirst': 0.5, 'armsecond': 1.0, 'divisions': 2, 'anglestart':0})
            return render_template('main.html', test=data, imgs=imgs, e=e)
       



if __name__ == '__main__': app.run(debug=True)
