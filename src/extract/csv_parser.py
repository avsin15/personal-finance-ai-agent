import pandas as pd
from datetime import datetime

COMMON_DATE_FORMATS = ["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]

def parse_date_safe(s):
    for fmt in COMMON_DATE_FORMATS:
        try:
            return datetime.strptime(str(s), fmt).date()
        except Exception:
            continue
    try:
        return pd.to_datetime(s, errors="coerce").date()
    except Exception:
        return None

def load_csv(path, mapping=None):
    df = pd.read_csv(path)
    if mapping:
        df = df.rename(columns=mapping)

    cols = [c.lower() for c in df.columns]
    date_col = df.columns[0]
    desc_col = df.columns[1]
    amt_col = df.columns[2]

    df_out = pd.DataFrame({
        "tx_date": df[date_col].apply(parse_date_safe),
        "description": df[desc_col].astype(str),
        "amount": pd.to_numeric(df[amt_col], errors="coerce").fillna(0.0),
        "currency": "INR",
    })

    return df_out

