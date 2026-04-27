def churn_by_contract(df):
    return (
        df.groupby("Contract")["ChurnFlag"]
        .mean()
        .sort_values(ascending=False) * 100
    )

def churn_by_payment(df):
    return (
        df.groupby("PaymentMethod")["ChurnFlag"]
        .mean()
        .sort_values(ascending=False) * 100
    )