import pandas as pd

def transform(df):
    df.drop_duplicates(ignore_index=True, inplace=True)

    df.loc[df["City"].isna(), "City"] = "N/A"

    df.loc[df["Quantity"].isna(), "Quantity"] = 0.0

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    df["Revenue"] = df["Price"] * df["Quantity"]
    return df