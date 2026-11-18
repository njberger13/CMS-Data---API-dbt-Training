
WITH ranked_reports AS (

    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY provider_ccn
            ORDER BY
                fiscal_year_end DESC,
                report_record_number DESC
        ) AS report_rank

    FROM {{ ref('int_hospital_financials') }}

),

latest_hospital_reports AS (

    SELECT *
    FROM ranked_reports
    WHERE report_rank = 1

)

SELECT
    state_code,

    COUNT(DISTINCT provider_ccn) AS hospital_count,

    SUM(net_patient_revenue) AS total_net_patient_revenue,
    AVG(net_patient_revenue) AS average_net_patient_revenue,

    SUM(net_income_from_service_to_patients) AS total_net_income_from_service_to_patients,
    AVG(net_income_from_service_to_patients) AS average_net_income_from_service_to_patients,

    SUM(net_income) AS total_net_income,
    AVG(net_income) AS average_net_income,

    AVG(operating_margin) AS average_operating_margin,
    AVG(net_income_margin) AS average_net_income_margin,
    AVG(npr_per_discharge) AS average_revenue_per_discharge

FROM latest_hospital_reports

GROUP BY state_code
