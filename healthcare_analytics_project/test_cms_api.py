import requests

url = "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data"

batch_size = 5000
offset = 130000
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