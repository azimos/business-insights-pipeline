def build_daily_metrics(df):
    daily = df.groupby("date").agg({
        "revenue": "sum"
    }).reset_index()

    daily = daily.sort_values("date")

    # Add rolling average
    daily["rolling_avg"] = daily["revenue"].rolling(window=3, min_periods=1).mean()

    # % change
    daily["pct_change"] = daily["revenue"].pct_change().fillna(0)

    return daily
