import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna(subset=["TotalCharges"])

    df["ChurnFlag"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df