from src.ingestion import load_sales_data
from src.transform import build_daily_metrics
from src.anomaly_detection import detect_anomalies
from src.llm_insights import generate_insights
from src.visualization import plot_revenue

def run_pipeline():
    df = load_sales_data()

    df_metrics = build_daily_metrics(df)

    df_analyzed = detect_anomalies(df_metrics)

    insights = generate_insights(df_analyzed)

    print(insights)

    with open("outputs/insights.txt", "w") as f:
        f.write(insights)

    plot_revenue(df_analyzed)

if __name__ == "__main__":
    run_pipeline()
