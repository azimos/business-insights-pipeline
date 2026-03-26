import plotly.express as px

def plot_revenue(df):
    fig = px.line(
        df,
        x="date",
        y="revenue",
        title="Revenue Over Time"
    )

    # highlight anomalies
    anomalies = df[df["anomaly"] == -1]

    fig.add_scatter(
        x=anomalies["date"],
        y=anomalies["revenue"],
        mode="markers",
        name="Anomalies"
    )

    fig.write_html("outputs/charts.html")
