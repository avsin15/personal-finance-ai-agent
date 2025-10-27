import pandas as pd

def totals_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Category")["amount"].sum().sort_values(ascending=False).reset_index()

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    df["month"] = pd.to_datetime(df["tx_date"]).dt.to_period("M").astype(str)
    return df.groupby(["month", "Category"])["amount"].sum().reset_index()

def savings_estimate(df: pd.DataFrame, pct: float = 0.1) -> float:
    expenses = df[df["amount"] > 0]["amount"].sum()
    return round(expenses * pct, 2)

