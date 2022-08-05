import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

def graphJSON():
    df = pd.DataFrame({'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],  'Amount': [4, 1, 2, 2, 4, 5], 'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})   
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')   
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def graphJSON1():
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
    return graphJSON1