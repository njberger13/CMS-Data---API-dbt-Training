SELECT *
FROM {{ ref('stg_cost_reports') }}
WHERE gross_revenue - contractual_allowances_and_discounts <> net_patient_revenue