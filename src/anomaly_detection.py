def detect_anomalies(df):
    from sklearn.ensemble import IsolationForest

    model = IsolationForest(contamination=0.1, random_state=42)

    features = df[["revenue", "pct_change"]]

    df["anomaly"] = model.fit_predict(features)

    return df
