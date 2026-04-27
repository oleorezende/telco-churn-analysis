from src.load_data import load_data
from src.analysis import churn_by_contract, churn_by_payment

def main():
    df = load_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    print("Churn por contrato:")
    print(churn_by_contract(df))

    print("\nChurn por pagamento:")
    print(churn_by_payment(df))

if __name__ == "__main__":
    main()