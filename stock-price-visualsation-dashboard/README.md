Stock Price Visualization Dashboard


Objective:-

The objective of this project is to analyze and visualize stock market data using Python.
This project helps users understand stock price movements, trading volume, and technical indicators such as Moving Average (MA20) and Relative Strength Index (RSI).

It is useful for beginners in data analysis and financial analytics.

Project Description:-

This project fetches historical stock data using the Yahoo Finance API (yfinance) and processes it using Python.
The data is then used to calculate technical indicators and generate visual charts.

The main focus of this project is:-

Stock price trend analysis
Volume analysis
Technical indicator calculation
Data visualization using Matplotlib

Dataset Information:-

The dataset is collected using the Yahoo Finance API.

It includes the following columns:-

Open
High
Low
Close
Adj Close
Volume

Example stock used:-

Apple (AAPL)
Tesla (TSLA)
Microsoft (MSFT)

Tools and Libraries Used:-

Python 
Pandas 
NumPy 
Matplotlib 
yfinance 
ta (Technical Analysis Library)

Features of the Project:-

Fetch real-time historical stock data
Save data into CSV file
Plot stock closing price
Plot trading volume
Calculate Moving Average (MA20)
Calculate Relative Strength Index (RSI)
Visualize technical indicators

Technical Indicators Explained:-

Moving Average (MA20):-

Moving Average is used to smooth out price data and identify trends.

Formula used:

MA20 = Average of last 20 closing prices

Usage:

Helps identify upward or downward trends in stock prices

Relative Strength Index (RSI):-

RSI is a momentum indicator that measures speed and change of price movements.

Values:

Above 70 → Overbought (price may fall)
Below 30 → Oversold (price may rise)

Project Structure:-

stock-dashboard/
│
├── app.py 
├── indicators.py
├── Data/
│     └── AAPL_Stock_Data.csv
├── screenshots/
├── README.md
└── requirements.txt

How to Run the Project(powershell):-

Install dependencies:-
pip install -r requirements.txt

Run Python file:- 
python app.py

Requirements:-

dash
plotly
yfinance
pandas
numpy
ta

Output Description

After running the project, you will see:

Stock price trend graph
Volume distribution graph
Moving Average line over stock price
RSI indicator graph with 30–70 levels


Conclusion:- 

This project demonstrates how to collect, process, and visualize stock market data using Python.
It helps in understanding financial trends and introduces technical indicators used in trading analysis.

Author:-

Student Project – Stock Market Analysis Dashboard
Built using Python and Yahoo Finance API


