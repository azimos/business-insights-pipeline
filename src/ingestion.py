import pandas as pd

def load_sales_data(file_path="data/raw/sales.csv"):
    df = pd.read_csv(file_path, parse_dates=["date"])
    return df
