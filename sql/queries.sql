-- ===============================
-- Churn por tipo de contrato
-- ===============================
SELECT 
    Contract,
    COUNT(*) AS total_clientes,
    SUM(ChurnFlag) AS clientes_churn,
    ROUND(AVG(ChurnFlag) * 100, 2) AS taxa_churn
FROM clientes
GROUP BY Contract
ORDER BY taxa_churn DESC;


-- ===============================
-- Churn por método de pagamento
-- ===============================
SELECT 
    PaymentMethod,
    COUNT(*) AS total_clientes,
    SUM(ChurnFlag) AS clientes_churn,
    ROUND(AVG(ChurnFlag) * 100, 2) AS taxa_churn
FROM clientes
GROUP BY PaymentMethod
ORDER BY taxa_churn DESC;


-- ===============================
-- Churn por serviço de internet
-- ===============================
SELECT 
    InternetService,
    COUNT(*) AS total_clientes,
    SUM(ChurnFlag) AS clientes_churn,
    ROUND(AVG(ChurnFlag) * 100, 2) AS taxa_churn
FROM clientes
GROUP BY InternetService
ORDER BY taxa_churn DESC;


-- ===============================
-- Churn por tempo de cliente
-- ===============================
SELECT
    CASE 
        WHEN tenure <= 6 THEN '0 a 6 meses'
        WHEN tenure <= 12 THEN '7 a 12 meses'
        WHEN tenure <= 24 THEN '13 a 24 meses'
        WHEN tenure <= 48 THEN '25 a 48 meses'
        ELSE '49+ meses'
    END AS faixa_tempo_cliente,
    COUNT(*) AS total_clientes,
    SUM(ChurnFlag) AS clientes_churn,
    ROUND(AVG(ChurnFlag) * 100, 2) AS taxa_churn
FROM clientes
GROUP BY faixa_tempo_cliente
ORDER BY taxa_churn DESC;