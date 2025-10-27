import pandas as pd
from src.categorize.rules import rule_category

def categorize_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Category"] = df["description"].apply(lambda d: rule_category(d) or "Others")
    return df
