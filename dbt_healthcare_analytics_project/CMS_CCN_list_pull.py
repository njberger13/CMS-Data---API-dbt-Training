import requests

url = "https://data.cms.gov/data-api/v1/dataset/8ba0f9b4-9493-4aa0-9f82-44ea9468d1b5/data"

batch_size = 5000
offset = 0
all_records = []

while True:

    params = {
        "size": batch_size,
        "offset": offset
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    batch = response.json()

    if not batch:
        break

    all_records.extend(batch)

    print(f"Retrieved {len(batch)} records. Total: {len(all_records)}")

    offset += len(batch)

    if len(batch) < batch_size:
        break

print(f"\nCOMPLETE: Retrieved {len(all_records)} records.")

for record in all_records[:1]:
    print(record)