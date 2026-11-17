SELECT *
FROM {{ ref('stg_cost_reports') }}
WHERE total_income - total_other_expenses <> net_income