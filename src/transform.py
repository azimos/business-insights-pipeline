def build_metrics(df):
    # ---- DAILY METRICS ----
    daily = (
        df.groupby("date")
        .agg(revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("date")
    )

    daily["rolling_avg"] = daily["revenue"].rolling(window=7, min_periods=1).mean()
    daily["pct_change"] = daily["revenue"].pct_change().fillna(0)

    # ---- PRODUCT METRICS ----
    product = (
        df.groupby(["date", "product"])
        .agg(revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("date")
    )

    return daily, product
