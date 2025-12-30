import os
import pandas as pd

BRONZE_FILE = "data/bronze/bronze_sample.csv"
SILVER_DIR = "data/silver"

def build_silver():
    os.makedirs(SILVER_DIR, exist_ok=True)

    df = pd.read_csv(BRONZE_FILE)

    # basic data quality checks
    df = df.dropna(subset=["name"])
    df["amount"] = df["amount"].astype(int)
    df = df.drop_duplicates()

    out = os.path.join(SILVER_DIR, "silver_sample.csv")
    df.to_csv(out, index=False)
    print(f"Wrote silver data -> {out}")

if __name__ == "__main__":
    build_silver()

