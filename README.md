# Stock Marketing Project
## Overview

This repository contains two stock market analysis projects developed using Python:

1. Algorithmic Trading Bot (Primary Project)

An intelligent stock analysis system that evaluates stocks using multiple technical and fundamental indicators.

2. Stock Price Visualization Dashboard (Secondary Project)

An interactive dashboard for visualizing stock market trends and technical indicators.

## Main Project: Algorithmic Trading Bot
### Features

Real-time stock data collection using Yahoo Finance
Relative Strength Index (RSI) Analysis
Momentum Analysis
Piotroski Score Evaluation
Buy / Hold / Sell Signal Generation
Automated PDF Report Generation
Stock Performance Visualization
CSV Data Export

### Stocks Analyzed 

Apple (AAPL)
Microsoft (MSFT)
Google (GOOGL)
NVIDIA (NVDA)
Meta (META)

### Technologies Used

Python
Pandas
NumPy
yFinance
Matplotlib
FPDF
Jupyter Notebook

### Project Structure
algorithmic-trading-bot/
│
├── data/
├── reports/
├── notebook/
│   └── stock_analysis.ipynb
├── src/
├── requirements.txt
└── README.md



## Secondary Project: Stock Price Visualization Dashboard
### Features

Interactive Dashboard
Moving Average Analysis
RSI Visualization
Dynamic Stock Selection
Responsive UI Design
Plotly Graphs

### Technologies Used

Dash
Plotly
Pandas
yFinance

### Sample Analysis 
Indicators Used                                       Indicator	Purpose

RSI                                                 	Measures overbought and oversold conditions
Momentum	                                            Identifies trend strength
Moving Average	                                      Determines market direction
Piotroski Score	                                      Evaluates company financial strength


### Installation
git clone https://github.com/suryarp1580-cmyk/Stock-Marketing-Project.git

cd Stock-Marketing-Project

pip install -r requirements.txt

## Running the Projects

Algorithmic Trading Bot:- (major project details)
python main.py  -----> main project details
python backtest.py
python piotroski_score.py
python momentum_strategy.py

Stock Price Visualization Dashboard:- (minor project)
python Dashboard.py]
python app.py      ] -------> both are main project details
py indicators.py

### Then open:

http://127.0.0.1:8050

### Future Enhancements

Machine Learning Stock Prediction
Portfolio Optimization
Live Market Streaming
Risk Analysis Module
AI-Based Trading Recommendations

# Author

Suryaraj S

GitHub: https://github.com/suryarp1580-cmyk

One more suggestion: your repository currently contains two separate projects inside one repo. For a stronger portfolio, recruiters usually prefer:

Stock-Marketing-Project
│
├── algorithmic-trading-bot   ----> Main Project
└── stock-price-visualisation-dashboard


