from ta.momentum import RSIIndicator
import pandas as pd

def add_indicators(df):

    df = df.copy()

   
    close = df['Close']
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    close = close.astype(float)

    df['MA20'] = close.rolling(window=20).mean()

    df['RSI'] = RSIIndicator(close=close, window=14).rsi()

    return df