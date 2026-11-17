-- ->> brings in as text

SELECT
    data ->> 'rpt_rec_num' AS id,
    data ->> 'Provider CCN' AS provider_ccn,
    (data ->> 'Fiscal Year Begin Date')::date AS fiscal_year_begin,
    (data ->> 'Fiscal Year End Date')::date AS fiscal_year_end,
    NULLIF(data ->> 'Total Days (V + XVIII + XIX + Unknown)', '')::BIGINT AS total_days,
    NULLIF(data ->> 'Number of Beds', '')::BIGINT AS bed_count,
    NULLIF(data ->> 'Total Discharges (V + XVIII + XIX + Unknown)', '')::BIGINT AS total_discharges,
    NULLIF(data ->> 'Inpatient Revenue', '')::BIGINT AS inpatient_revenue,
    NULLIF(data ->> 'Outpatient Revenue', '')::BIGINT AS outpatient_revenue,
    NULLIF(data ->> 'Total Patient Revenue', '')::BIGINT AS gross_revenue,
    NULLIF(data ->> 'Less Contractual Allowance and Discounts on Patients'' Accounts', '')::BIGINT AS contractual_allowances_and_discounts,
    NULLIF(data ->> 'Net Patient Revenue', '')::BIGINT AS net_patient_revenue,
    NULLIF(data ->> 'Less Total Operating Expense', '')::BIGINT AS operating_expense,
    NULLIF(data ->> 'Net Income from Service to Patients', '')::BIGINT AS net_income_from_service_to_patients,
    NULLIF(data ->> 'Total Other Income', '')::BIGINT AS total_other_income,
    NULLIF(data ->> 'Total Income', '')::BIGINT AS total_income,
    NULLIF(data ->> 'Total Other Expenses', '')::BIGINT AS total_other_expenses,
    NULLIF(data ->> 'Net Income', '')::BIGINT AS net_income

FROM {{ source('cms_raw', 'cost_report_data') }}