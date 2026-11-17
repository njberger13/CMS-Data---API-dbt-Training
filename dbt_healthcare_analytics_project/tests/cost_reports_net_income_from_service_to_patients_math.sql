SELECT *
FROM {{ ref('stg_cost_reports') }}
WHERE net_patient_revenue - operating_expense <> net_income_from_service_to_patients