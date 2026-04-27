def churn_by_contract(df):
    result = df.groupby("Contract").agg(
        total_clientes=("customerID", "count"),
        clientes_churn=("ChurnFlag", "sum"),
        taxa_churn=("ChurnFlag", "mean")
    ).reset_index()

    result["taxa_churn"] = result["taxa_churn"] * 100

    return result.sort_values("taxa_churn", ascending=False)


def churn_by_payment(df):
    result = df.groupby("PaymentMethod").agg(
        total_clientes=("customerID", "count"),
        clientes_churn=("ChurnFlag", "sum"),
        taxa_churn=("ChurnFlag", "mean")
    ).reset_index()

    result["taxa_churn"] = result["taxa_churn"] * 100

    return result.sort_values("taxa_churn", ascending=False)