import pandas as pd
import re

def normalize(df):
    df = df.copy()
    df["description"] = (
        df["description"]
        .astype(str)
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r"[^A-Za-z0-9\s\-]", "", regex=True)
        .str.strip()
        .str.lower()
    )
    return df
