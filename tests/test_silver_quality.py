import pandas as pd

def test_no_null_names():
    df = pd.read_csv("data/silver/silver_sample.csv")
    assert df["name"].isna().sum() == 0
