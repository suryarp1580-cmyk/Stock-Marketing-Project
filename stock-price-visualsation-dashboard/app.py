import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from indicators import add_indicators

stock = yf.download("AAPL", start="2024-01-01", end="2026-01-01")

if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

stock.to_csv("Data/AAPL_Stock_Data.csv")

data = add_indicators(stock.copy())

data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
data['Volume'] = pd.to_numeric(data['Volume'], errors='coerce')

plt.figure(figsize=(12,6))
plt.plot(data["Close"])
plt.title("Apple Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(data['Volume'])
plt.title("Volume Chart")
plt.grid()
plt.show()

plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close')
plt.plot(data['MA20'], label='MA20')
plt.legend()
plt.title("Moving Average (MA20)")
plt.grid()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(data['RSI'], label='RSI')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.legend()
plt.title("RSI Indicator")
plt.grid()
plt.show()

print(data.columns)
print(data[['Close', 'MA20', 'RSI']].head(20))