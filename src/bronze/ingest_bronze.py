import os
import pandas as pd

RAW_FILE = "data/raw/sample.csv"
BRONZE_DIR = "data/bronze"

def ingest_bronze():
    os.makedirs(BRONZE_DIR, exist_ok=True)
    df = pd.read_csv(RAW_FILE)
    out = os.path.join(BRONZE_DIR, "bronze_sample.csv")
    df.to_csv(out, index=False)
    print(f"Wrote bronze data -> {out}")

if __name__ == "__main__":
    ingest_bronze()

