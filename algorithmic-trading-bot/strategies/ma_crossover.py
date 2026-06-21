def add_ma_crossover(data):

    data["Signal"] = 0

    data.loc[
        data["MA20"] > data["MA50"],
        "Signal"
    ] = 1

    data.loc[
        data["MA20"] < data["MA50"],
        "Signal"
    ] = -1

    data["Position"] = data["Signal"].diff()

    return data