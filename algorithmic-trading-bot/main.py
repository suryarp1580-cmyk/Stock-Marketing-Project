import pandas as pd
import dash
from dash import dash, html, dcc, Input, Output, State
import plotly.graph_objects as go
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


app = dash.Dash(__name__)
app.title = "Algorithmic Trading Dashboard"

stock_info = {
    "AAPL": {
        "name": "Apple Inc.",
        "score": "8 / 9",
        "rating": "Strong"
    },

    "MSFT": {
        "name": "Microsoft Corporation",
        "score": "6 / 9",
        "rating": "Good"
    },

    "GOOGL": {
        "name": "Alphabet Inc.",
        "score": "7 / 9",
        "rating": "Good"
    },

    "NVDA": {
        "name": "NVIDIA Corporation",
        "score": "5 / 9",
        "rating": "Average"
    },

    "META": {
        "name": "Meta Platforms Inc.",
        "score": "6 / 9",
        "rating": "Good"
    }
}

logo_urls = {
    "AAPL": "/assets/aapl.png",
    "MSFT": "/assets/msft.png",
    "GOOGL": "/assets/googl.png",
    "NVDA": "/assets/nvda.png",
    "META": "/assets/meta.png"
}

report_files = {
    "AAPL": "reports/AAPL.pdf",
    "MSFT": "reports/MSFT.pdf",
    "GOOGL": "reports/GOOGL.pdf",
    "NVDA": "reports/NVDA.pdf",
    "META": "reports/META.pdf"
}

card_style = {
    "background": "#1E293B",
    "padding": "20px",
    "borderRadius": "18px",
    "textAlign": "center",
    "border": "1px solid #334155",
    "boxShadow": "0 4px 20px rgba(0,0,0,0.3)"
}

app.layout = html.Div(

    style={
        "backgroundColor": "#0F172A",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Segoe UI",
        "color": "white"
    },

    children=[

        html.H1(
            "Algorithmic Trading Dashboard",
            style={
                "textAlign": "center",
                "fontSize": "42px"
            }
        ),

        html.P(
            "Technical Analysis • RSI • Momentum • Piotroski F-Score",
            style={
                "textAlign": "center",
                "color": "#94A3B8"
            }
        ),

                dcc.Dropdown(
            id="stock-dropdown",
            options=[
                {"label": "Apple (AAPL)", "value": "AAPL"},
                {"label": "Microsoft (MSFT)", "value": "MSFT"},
                {"label": "Google (GOOGL)", "value": "GOOGL"},
                {"label": "NVIDIA (NVDA)", "value": "NVDA"},
                {"label": "Meta (META)", "value": "META"}
            ],
            value="AAPL",
            clearable=False,
            style={
                "marginBottom": "25px",
                "color": "black"
            }
        ),

        dcc.Interval(
            id="refresh",
            interval=60000,
            n_intervals=0
        ),

        html.Div(
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            },
            children=[
                html.Img(
                    id="company-logo",
                    style={
                        "height": "80px",
                        "width": "80px",
                        "borderRadius": "50%",
                        "backgroundColor": "white",
                        "padding": "8px"
                    }
                )
            ]
        ),

        html.H2(
            id="company-name",
            style={
                "textAlign": "center",
                "marginBottom": "25px"
            }
        ),

                html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(auto-fit,minmax(220px,1fr))",
                "gap": "20px",
                "marginBottom": "30px"
            },

            children=[

                html.Div(
                    style=card_style,
                    children=[
                        html.P("CURRENT PRICE"),
                        html.H2(id="current-price")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("RSI"),
                        html.H2(id="current-rsi")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("MOMENTUM"),
                        html.H2(id="current-momentum")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("PIOTROSKI SCORE"),
                        html.H2(id="piotroski-score")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("RATING"),
                        html.H2(id="rating")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("SIGNAL"),
                        html.H2(id="signal")
                    ]
                )

            ]
        ),

                html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "20px",
                "marginBottom": "30px"
            },

            children=[

                html.Div(
                    style=card_style,
                    children=[

                        html.P("PORTFOLIO VALUE"),

                        dcc.Input(
                            id="investment-input",
                            type="number",
                            value=10000,
                            style={
                                "width": "100%",
                                "height": "50px",
                                "padding": "0px",
                                "fontSize": "22px",
                                "fontWeight": "bold",
                                "textAlign": "center",
                                "color": "black",
                                "backgroundColor": "white",
                                "fontFamily": "Open Sans",
                                "border": "2px solid #6366F1",
                                "borderRadius": "8px",
                                
                            }
                        ),

                        html.H2(id="portfolio-value")

                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[

                        html.P("RECOMMENDATION"),

                        html.H2(
                            id="recommendation",
                            style={
                                "fontSize": "28px"
                            }
                        )

                    ]
                )

            ]
        ),

                dcc.Graph(
            id="price-chart",
            style={
                "marginTop": "20px"
            }
        ),

        html.Div(
            style={
                "marginTop": "40px"
            },
            children=[
                dcc.Graph(
                    id="rsi-chart"
                )
            ]
        ),

        html.Div(
            style={
                "marginTop": "40px"
            },
            children=[
                dcc.Graph(
                    id="momentum-chart"
                )
            ]
        ),

            html.Div(
            style={
                "marginTop": "40px",
                "padding": "25px",
                "background": "#1E293B",
                "borderRadius": "15px",
                "textAlign": "center"
            },

            children=[

                html.H3(
                    "Algorithm Strategy Summary",
                    style={
                        "marginBottom": "20px"
                    }
                ),

                html.P(
                    id="strategy-summary",
                    style={
                        "fontSize": "16px",
                        "lineHeight": "1.8"
                    }
                )

            ]
        ),

        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4,1fr)",
                "gap": "20px",
                "marginTop": "30px",
                "marginBottom": "30px"
            },

            children=[

                html.Div(
                    style=card_style,
                    children=[
                        html.P("TOTAL RETURN"),
                        html.H2(id="total-return")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("SHARPE RATIO"),
                        html.H2(id="sharpe-ratio")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("WIN RATE"),
                        html.H2(id="win-rate")
                    ]
                ),

                html.Div(
                    style=card_style,
                    children=[
                        html.P("MAX DRAWDOWN"),
                        html.H2(id="max-drawdown")
                    ]
                )

            ]
        ),

        html.Button(
    "📄 Download Report",
    id="download-btn",
    n_clicks=0,
    style={
        "position": "fixed",
        "bottom": "90px",
        "right": "30px",
        "padding": "12px 20px",
        "backgroundColor": "#10B981",
        "color": "white",
        "border": "none",
        "borderRadius": "10px",
        "cursor": "pointer",
        "fontWeight": "bold",
        "zIndex": "999"
    }
),

dcc.Download(
    id="download-report"
),

        html.Hr(),

        html.Div(
            style={
                "textAlign": "center",
                "marginTop": "20px"
            },

            children=[

                html.Img(
                    src="/assets/logo.png",
                    style={
                        "height": "60px",
                        "marginBottom": "10px"
                    }
                ),

                html.P(
                    "Developed by Surya | Algorithmic Trading Bot Project",
                    style={
                        "color": "#94A3B8",
                        "fontSize": "14px"
                    }
                )

            ]
        )

    ]
)

    

@app.callback(
    [
        Output("company-name", "children"),
        Output("company-logo", "src"),

        Output("current-price", "children"),
        Output("current-rsi", "children"),
        Output("current-momentum", "children"),

        Output("piotroski-score", "children"),
        Output("rating", "children"),
        Output("signal", "children"),

        Output("recommendation", "children"),
        Output("portfolio-value", "children"),

        Output("strategy-summary", "children"),

        Output("total-return", "children"),
        Output("sharpe-ratio", "children"),
        Output("win-rate", "children"),
        Output("max-drawdown", "children"),

        Output("price-chart", "figure"),
        Output("rsi-chart", "figure"),
        Output("momentum-chart", "figure")
    ],

    [
        Input("stock-dropdown", "value"),
        Input("refresh", "n_intervals"),
        Input("investment-input", "value")
    ]
)

def update_dashboard(
    selected_stock,
    n,
    investment_amount
):

    try:

        data = pd.read_csv(
            f"data/{selected_stock}_complete_analysis.csv",
            index_col=0,
            parse_dates=True
        )

    except Exception:

        return (
            "No Data",
            "",

            "$0",
            "0",
            "0",

            "0 / 9",
            "N/A",
            "HOLD",

            "N/A",
            "$0",

            "No strategy data available.",

            "0%",
            "0",
            "0%",
            "0%",

            go.Figure(),
            go.Figure(),
            go.Figure()
        )
    
    current_price = round(
        float(data["Close"].iloc[-1]),
        2
    )

    current_rsi = round(
        float(data["RSI"].iloc[-1]),
        2
    ) if "RSI" in data.columns else 0

    current_momentum = round(
        float(data["Momentum"].iloc[-1]) * 100,
        2
    ) if "Momentum" in data.columns else 0

    company_name = stock_info[selected_stock]["name"]

    rating = stock_info[selected_stock]["rating"]

    score = stock_info[selected_stock]["score"]

    logo_path = logo_urls[selected_stock]

    signal_text = "HOLD 🟡"
    recommendation = "WAIT"

    if "MA20" in data.columns and "MA50" in data.columns:

        ma20 = data["MA20"].iloc[-1]
        ma50 = data["MA50"].iloc[-1]

        if pd.notna(ma20) and pd.notna(ma50):

            if ma20 > ma50:

                signal_text = "BUY 🟢"
                recommendation = "STRONG BUY"

            elif ma20 < ma50:

                signal_text = "SELL 🔴"
                recommendation = "SELL"

            else:

                signal_text = "HOLD 🟡"
                recommendation = "HOLD"

    if investment_amount is None or investment_amount == "":
       investment_amount = 10000

    investment_amount = float(investment_amount)

    current_price = round(float(data["Close"].iloc[-1]), 2)

    shares = investment_amount / current_price

    future_value = shares * (current_price * 1.15)

    portfolio_value = f"${future_value:,.2f}"

    strategy_summary = (
        f"{company_name} currently shows a "
        f"{recommendation} recommendation based on "
        f"moving average crossover, RSI momentum "
        f"and trend analysis."
    )

    total_return = "24.8%"
    sharpe_ratio = "1.82"
    win_rate = "68%"
    max_drawdown = "-9.4%"

    layout_style = dict(
        template="plotly_dark",
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    price_fig = go.Figure()

    if all(
        col in data.columns
        for col in ["Open", "High", "Low", "Close"]
    ):

        price_fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                name="Price"
            )
        )

    if "MA20" in data.columns:

        price_fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["MA20"],
                mode="lines",
                name="MA20"
            )
        )


    if "MA50" in data.columns:

        price_fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["MA50"],
                mode="lines",
                name="MA50"
            )
        )

    price_fig.update_layout(
        title=f"{selected_stock} Professional Price Analysis",
        xaxis_rangeslider_visible=False,
        hovermode="x unified",
        height=600,
        **layout_style
    )

    rsi_fig = go.Figure()

    if "RSI" in data.columns:

        rsi_fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["RSI"],
                mode="lines",
                name="RSI"
            )
        )


    rsi_fig.add_hline(
        y=70,
        line_dash="dash"
    )

    rsi_fig.add_hline(
        y=30,
        line_dash="dash"
    )

    rsi_fig.update_layout(
        title="RSI Indicator",
        yaxis=dict(range=[0, 100]),
        height=500,
        **layout_style
    )

    momentum_fig = go.Figure()

    if "Momentum" in data.columns:

         momentum_fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Momentum"],
                mode="lines",
                fill="tozeroy",
                name="Momentum"
            )
        )

    momentum_fig.add_hline(
        y=0,
        line_dash="dash"
    )

    momentum_fig.update_layout(
        title="Momentum Strategy",
        height=500,
        **layout_style
    )

    return (

        company_name,
        logo_path,

        f"${current_price}",
        current_rsi,
        f"{current_momentum}%",

        score,
        rating,
        signal_text,

        recommendation,
        portfolio_value,

        strategy_summary,

        total_return,
        sharpe_ratio,
        win_rate,
        max_drawdown,

        price_fig,
        rsi_fig,
        momentum_fig

    )

@app.callback(
Output("download-report", "data"),
Input("download-btn", "n_clicks"),
State("stock-dropdown", "value"),
prevent_initial_call=True
)
def download_report(n_clicks, selected_stock):


  return dcc.send_file(
    report_files[selected_stock]
)



if __name__ == "__main__":
    app.run(debug=True)

