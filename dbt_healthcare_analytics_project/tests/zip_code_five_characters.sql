SELECT *
FROM {{ ref('stg_pos_qies') }}
WHERE zip_code !~ '^[0-9]{5}$'