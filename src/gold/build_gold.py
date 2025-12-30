import os
import pandas as pd

SILVER_FILE = "data/silver/silver_sample.csv"
GOLD_DIR = "data/gold"

def build_gold():
    os.makedirs(GOLD_DIR, exist_ok=True)

    df = pd.read_csv(SILVER_FILE)
    summary = df.groupby("name", as_index=False)["amount"].sum()

    out = os.path.join(GOLD_DIR, "gold_summary.csv")
    summary.to_csv(out, index=False)
    print(f"Wrote gold data -> {out}")

if __name__ == "__main__":
    build_gold()

