def add_momentum_strategy(data):

    data["Momentum"] = data["Close"].pct_change(90)

    data["Momentum_Signal"] = 0

    data.loc[
        data["Momentum"] > 0.15,
        "Momentum_Signal"
    ] = 1

    data.loc[
        data["Momentum"] < -0.15,
        "Momentum_Signal"
    ] = -1

    return data