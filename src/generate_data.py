import pandas as pd
import numpy as np

def generate_sales_data(num_days=60):
    np.random.seed(42)

    dates = pd.date_range(end=pd.Timestamp.today(), periods=num_days)

    products = ["Product A", "Product B", "Product C"]

    data = []

    for date in dates:
        for product in products:
            base = {
                "Product A": 200,
                "Product B": 150,
                "Product C": 100
            }[product]

            # Add normal variation
            revenue = base + np.random.normal(0, 30)

            # Inject realistic anomalies
            if np.random.rand() < 0.05:
                revenue *= np.random.choice([0.3, 2.5])  # drop or spike

            data.append({
                "date": date,
                "product": product,
                "revenue": max(0, round(revenue, 2)),
                "customer_id": np.random.randint(1, 200)
            })

    df = pd.DataFrame(data)

    df.to_csv("data/raw/sales.csv", index=False)

    print("✅ Generated dataset with", len(df), "rows")


if __name__ == "__main__":
    generate_sales_data()
