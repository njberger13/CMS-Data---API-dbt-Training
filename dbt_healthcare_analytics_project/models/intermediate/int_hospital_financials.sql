
SELECT
    cr.id AS report_record_number,
    cr.provider_ccn,

    -- Facility identification and location
    p.facility_name,
    p.street_address,
    p.city,
    p.state_code,
    p.zip_code,
    p.cbsa_code,

    -- Reporting period
    cr.fiscal_year_begin,
    cr.fiscal_year_end,

    -- Operational metrics
    cr.total_days,
    cr.bed_count,
    cr.total_discharges,

    -- Financial metrics
    cr.gross_revenue,
    cr.contractual_allowances_and_discounts,
    cr.net_patient_revenue,
    cr.operating_expense,
    cr.net_income_from_service_to_patients,
    cr.total_other_income,
    cr.total_income,
    cr.total_other_expenses,
    cr.net_income,

    -- Calculated metrics
    ROUND(
        cr.net_income_from_service_to_patients::NUMERIC
        / NULLIF(cr.net_patient_revenue, 0),
        4
    ) AS operating_margin,

    ROUND(
        cr.net_income::NUMERIC
        / NULLIF(cr.net_patient_revenue, 0),
        4
    ) AS net_income_margin,

    ROUND(
        cr.net_patient_revenue::NUMERIC
        / NULLIF(cr.total_discharges, 0),
        2
    ) AS npr_per_discharge

FROM {{ ref('stg_cost_reports') }} cr

LEFT JOIN {{ ref('stg_pos_qies') }} p
    ON cr.provider_ccn = p.provider_number
