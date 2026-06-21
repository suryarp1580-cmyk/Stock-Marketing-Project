import yfinance as yf

tickers = [
    "AAPL",
    "NVDA",
    "GOOGL" 
]

for ticker in tickers:

    stock = yf.Ticker(ticker)

    income = stock.income_stmt
    balance = stock.balance_sheet
    cashflow = stock.cashflow

    score = 0

    try:
        net_income = income.loc["Net Income"].iloc[0]

        if net_income > 0:
            score += 1
    except:
        pass

    try:
        operating_cashflow = cashflow.loc["Operating Cash Flow"].iloc[0]

        if operating_cashflow > 0:
            score += 1
    except:
        pass

    try:
        total_assets = balance.loc["Total Assets"].iloc[0]

        roa = net_income / total_assets

        if roa > 0:
            score += 1
    except:
        pass

    try:
        if operating_cashflow > net_income:
            score += 1
    except:
        pass

    try:
        long_term_debt = balance.loc["Long Term Debt"].iloc[0]

        if long_term_debt < balance.loc["Long Term Debt"].iloc[1]:
            score += 1
    except:
        pass

    try:
        current_assets = balance.loc["Current Assets"].iloc[0]

        current_liabilities = balance.loc["Current Liabilities"].iloc[0]

        current_ratio_current = current_assets / current_liabilities

        previous_assets = balance.loc["Current Assets"].iloc[1]

        previous_liabilities = balance.loc["Current Liabilities"].iloc[1]

        current_ratio_previous = previous_assets / previous_liabilities

        if current_ratio_current > current_ratio_previous:
            score += 1
    except:
        pass

    try:
        shares_current = balance.loc["Ordinary Shares Number"].iloc[0]

        shares_previous = balance.loc["Ordinary Shares Number"].iloc[1]

        if shares_current <= shares_previous:
            score += 1
    except:
        pass

    try:
        gross_profit_current = income.loc["Gross Profit"].iloc[0]

        revenue_current = income.loc["Total Revenue"].iloc[0]

        gross_margin_current = gross_profit_current / revenue_current

        gross_profit_previous = income.loc["Gross Profit"].iloc[1]

        revenue_previous = income.loc["Total Revenue"].iloc[1]

        gross_margin_previous = gross_profit_previous / revenue_previous

        if gross_margin_current > gross_margin_previous:
            score += 1
    except:
        pass

    try:
        asset_turnover_current = revenue_current / total_assets

        previous_assets_total = balance.loc["Total Assets"].iloc[1]

        asset_turnover_previous = revenue_previous / previous_assets_total

        if asset_turnover_current > asset_turnover_previous:
            score += 1
    except:
        pass

    print("\n------------------------")
    print("Ticker:", ticker)
    print("Piotroski F-Score:", score, "/ 9")

    if score >= 8:
        print("Strong Company")

    elif score >= 6:
        print("Good Company")

    elif score >= 4:
        print("Average Company")

    else:
        print("Weak Company")