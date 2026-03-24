import plotly.express as px

def plot_revenue(df):
    fig = px.line(df, x="date", y="revenue", title="Daily Revenue")

    fig.write_html("outputs/charts.html")
