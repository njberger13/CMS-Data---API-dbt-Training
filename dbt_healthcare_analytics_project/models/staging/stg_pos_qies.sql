-- ->> brings in as text

SELECT
    data ->> 'PRVDR_NUM' AS provider_number,
    data ->> 'FAC_NAME' AS facility_name,
    data ->> 'ST_ADR' AS street_address,
    data ->> 'CITY_NAME' AS city,
    data ->> 'STATE_CD' AS state_code,
    data ->> 'ZIP_CD' AS zip_code,
    data ->> 'CBSA_CD' AS cbsa_code,
    data ->> 'PHN_NUM' AS phone_number,
    NULLIF(data ->> 'BED_CNT', '')::INTEGER AS bed_count

FROM {{ source('cms_raw', 'pos_qies') }}