SELECT *
FROM {{ ref('stg_cost_reports') }}
WHERE inpatient_revenue + outpatient_revenue <> gross_revenue