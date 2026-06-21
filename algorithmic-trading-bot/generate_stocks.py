import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

stocks = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "NVDA",
    "META"
]

for ticker in stocks:

    data = yf.download(
        ticker,
        start="2022-01-01",
        end="2026-01-01",
        auto_adjust=True
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data["MA20"] = data["Close"].rolling(20).mean()

    data["MA50"] = data["Close"].rolling(50).mean()

    data["RSI"] = RSIIndicator(
        close=data["Close"],
        window=14
    ).rsi()

    data["Momentum"] = data["Close"].pct_change(90)

    data.to_csv(
        f"data/{ticker}_complete_analysis.csv"
    )

    print(f"{ticker} saved successfully")