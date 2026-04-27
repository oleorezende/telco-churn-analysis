from src.load_data import load_data
from src.analysis import churn_by_contract, churn_by_payment
import sqlite3

def main():
    df = load_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    # 🗄️ CONECTA AO BANCO
    conn = sqlite3.connect("database.db")

    # 💾 SALVA DATAFRAME NO BANCO
    df.to_sql("clientes", conn, if_exists="replace", index=False)

    # 📊 ANALISES EM PYTHON
    contract = churn_by_contract(df)
    payment = churn_by_payment(df)

    print("Churn por contrato:")
    print(contract)

    print("\nChurn por pagamento:")
    print(payment)

    # 💾 SALVANDO RESULTADOS CSV
    contract.to_csv("output/churn_contract.csv", index=False)
    payment.to_csv("output/churn_payment.csv", index=False)

    # 🧠 QUERY SQL
    query = """
    SELECT 
        Contract,
        COUNT(*) AS total_clientes,
        SUM(ChurnFlag) AS clientes_churn,
        ROUND(AVG(ChurnFlag) * 100, 2) AS taxa_churn
    FROM clientes
    GROUP BY Contract
    ORDER BY taxa_churn DESC;
    """

    result = conn.execute(query).fetchall()

    print("\nResultado SQL:")
    print(result)

    conn.close()

if __name__ == "__main__":
    main()