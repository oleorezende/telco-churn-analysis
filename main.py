from src.load_data import load_data
from src.analysis import churn_by_contract, churn_by_payment

def main():
    df = load_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    contract = churn_by_contract(df)
    payment = churn_by_payment(df)

    print("Churn por contrato:")
    print(contract)

    print("\nChurn por pagamento:")
    print(payment)

    # 💾 SALVANDO RESULTADOS
    contract.to_csv("output/churn_contract.csv", index=False)
    payment.to_csv("output/churn_payment.csv", index=False)

if __name__ == "__main__":
    main()