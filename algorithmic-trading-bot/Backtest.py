import pandas as pd
from backtesting import Backtest
from backtesting import Strategy

data = pd.read_csv(
    "data/AAPL_complete_analysis.csv",
    index_col=0,
    parse_dates=True
)

data = data.dropna()

required_columns = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "MA20",
    "MA50",
    "RSI"
]

for column in required_columns:

    if column not in data.columns:
        raise ValueError(f"Missing column: {column}")

class MovingAverageRSIStrategy(Strategy):

    def init(self):
        pass

    def next(self):

        if (
            self.data.MA20[-1] > self.data.MA50[-1]
            and
            self.data.RSI[-1] < 70
        ):

            if not self.position:
                self.buy()

        elif (
            self.data.MA20[-1] < self.data.MA50[-1]
            or
            self.data.RSI[-1] > 70
        ):

            if self.position:
                self.position.close()

bt = Backtest(
    data,
    MovingAverageRSIStrategy,
    cash=100000,
    commission=0.002,
    exclusive_orders=True,
    finalize_trades=True
)

results = bt.run()

print("\n========== MA20 + MA50 + RSI BACKTEST RESULTS ==========\n")

print("Return [%]:", round(results["Return [%]"], 2))
print("Buy & Hold Return [%]:", round(results["Buy & Hold Return [%]"], 2))
print("Sharpe Ratio:", round(results["Sharpe Ratio"], 2))
print("Max Drawdown [%]:", round(results["Max. Drawdown [%]"], 2))
print("Win Rate [%]:", round(results["Win Rate [%]"], 2))
print("Number of Trades:", results["# Trades"])

results_df = pd.DataFrame(
    {
        "Metric": [
            "Return %",
            "Buy & Hold Return %",
            "Sharpe Ratio",
            "Max Drawdown %",
            "Win Rate %",
            "Number of Trades"
        ],
        "Value": [
            results["Return [%]"],
            results["Buy & Hold Return [%]"],
            results["Sharpe Ratio"],
            results["Max. Drawdown [%]"],
            results["Win Rate [%]"],
            results["# Trades"]
        ]
    }
)

results_df.to_csv(
    "reports/backtest_rsi_strategy.csv",
    index=False
)

print("\nReport Saved:")
print("reports/backtest_rsi_strategy.csv")

bt.plot()

