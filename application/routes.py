from application import app

from flask import render_template, url_for, request
import pandas as pd
import json
import plotly
import plotly.express as px

from datetime import date
import plotly.graph_objs as go
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ("AAPL", "GOOG", "MSFT", "GME", "BTC-USD", "ETH-USD")

n_years = 1
period = n_years * 365

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

#pandas data frame object
def df_train_data(data):
    df_train = data[['Date', 'Close']]
    
    return df_train.rename(columns={"Date": "ds", "Close":"y"})

def make_predict(df_train):
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    obj = {"m": m, "forecast":forecast}
    return obj

#data = load_data("BTC-USD")
#df_data = df_train_data(data)
#obj1 = make_predict(df_data)

#data2 = load_data("ETH-USD")
#df_data2 = df_train_data(data2)
#obj2 = make_predict(df_data2)

@app.route("/")
def index():
    # Generate graph
    graph1JSON = index_bitcoin()

    return render_template("index.html", title="Home", graph1JSON = graph1JSON, currency="Bitcoin")

@app.route("/search", methods=["GET"])
def search():
    args = request.args
    print(args)
    ticker = args.get('ticker')
    print(ticker)
    data = load_data(ticker)
    print(type(data))

    if data.empty:
        print("no data")
        return "ticker not found"

    df_data = df_train_data(data)

    obj1 = make_predict(df_data)
    

    fig2 = plot_plotly(obj1["m"], obj1["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON


@app.route("/bitcoin")
def index_bitcoin():
    # Generate graph
    data = load_data("BTC-USD")
    df_data = df_train_data(data)
    obj1 = make_predict(df_data)

    # update layout
    fig2 = plot_plotly(obj1["m"], obj1["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON

@app.route("/etherium")
def index_etherium():
    # Generate graph
    data2 = load_data("ETH-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON

@app.route("/tether")
def index_tether():
    # Generate graph
    data2 = load_data("USDT-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON

@app.route("/bnb")
def index_bnb():
    # Generate graph
    data2 = load_data("BNB-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON

@app.route("/usd-coin")
def index_usdc():
    # Generate graph
    data2 = load_data("USDC-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON
    
@app.route("/doge")
def index_doge():
    # Generate graph
    data2 = load_data("DOGE-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON

@app.route("/cardano")
def index_cardano():
    # Generate graph
    data2 = load_data("ADA-USD")
    df_data2 = df_train_data(data2)
    obj2 = make_predict(df_data2)

    # Graph Two
    fig2 = plot_plotly(obj2["m"], obj2["forecast"])
    fig2.update_layout(plot_bgcolor="#c4c66e")
    fig2.update_layout(paper_bgcolor="#000000")
    fig2.update_layout(       
        xaxis_title="Years",
        yaxis_title="Price ($)",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="White"
        )
    )
    fig2.update_xaxes(
        rangeselector_bgcolor="#000",
        rangeselector_bordercolor="#fff",
        rangeselector_borderwidth=1
    )
    graph1JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON