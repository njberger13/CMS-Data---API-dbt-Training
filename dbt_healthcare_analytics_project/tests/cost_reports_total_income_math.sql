SELECT *
FROM {{ ref('stg_cost_reports') }}
WHERE net_income_from_service_to_patients + total_other_income <> total_income