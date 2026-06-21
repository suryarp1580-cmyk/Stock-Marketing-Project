import yfinance as yf
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
from ta.momentum import RSIIndicator


def get_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)

    if df is None or df.empty:
        return pd.DataFrame()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.copy()
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    df['MA20'] = df['Close'].rolling(window=20).mean()

    try:
        df['RSI'] = RSIIndicator(close=df['Close'], window=14).rsi()
    except:
        df['RSI'] = None

    return df


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("📊 Stock Price Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Dropdown(
            id="stock-dropdown",
            options=[
                {"label": "Apple (AAPL)", "value": "AAPL"},
                {"label": "Tesla (TSLA)", "value": "TSLA"},
                {"label": "Microsoft (MSFT)", "value": "MSFT"}
            ],
            value="AAPL",
            style={"width": "48%"}
        ),

        dcc.DatePickerRange(
            id="date-range",
            start_date="2024-01-01",
            end_date="2026-01-01",
            style={"width": "48%"}
        )
    ], style={"display": "flex", "justifyContent": "space-between"}),

    html.Br(),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volume-chart"),
    dcc.Graph(id="ma-chart"),
    dcc.Graph(id="rsi-chart"),
])


@app.callback(
    [
        Output("price-chart", "figure"),
        Output("volume-chart", "figure"),
        Output("ma-chart", "figure"),
        Output("rsi-chart", "figure")
    ],
    [
        Input("stock-dropdown", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date")
    ]
)
def update_graph(symbol, start, end):

    df = get_data(symbol, start, end)

    if df.empty:
        empty_fig = go.Figure()
        empty_fig.update_layout(title="No Data Available")
        return empty_fig, empty_fig, empty_fig, empty_fig

    price_fig = go.Figure()
    price_fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Close"))
    price_fig.update_layout(title=f"{symbol} Stock Price")

    vol_fig = go.Figure()
    vol_fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume"))
    vol_fig.update_layout(title="Volume Chart")

    ma_fig = go.Figure()
    ma_fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Close"))
    ma_fig.add_trace(go.Scatter(x=df.index, y=df["MA20"], name="MA20"))
    ma_fig.update_layout(title="Moving Average (MA20)")

    rsi_fig = go.Figure()
    rsi_fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], name="RSI"))
    rsi_fig.add_hline(y=70, line_dash="dash", line_color="red")
    rsi_fig.add_hline(y=30, line_dash="dash", line_color="green")
    rsi_fig.update_layout(title="RSI Indicator")

    return price_fig, vol_fig, ma_fig, rsi_fig


if __name__ == "__main__":
    app.run(debug=True)