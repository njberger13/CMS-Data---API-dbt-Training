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

    # send HTTP GET request to API
    response = requests.get(url, params=params)
    
    # checks whether API request was successful (200 - successful, 400, 401, etc. are responses)
    # if response is 400+ (errors) then stops execution
    response.raise_for_status()

    # converts response to JSON. this will error if JSON is not the correct data type response
    batch = response.json()

    # if the batch retreived is empty (no records remaining), then exit
    if not batch:
        break

    all_records.extend(batch)

    print(f"Retrieved {len(batch)} records. Total: {len(all_records)}")

    offset += len(batch)

    # if the most recent batch was less than the batch size, it is the last one and can end the loop
    if len(batch) < batch_size:
        break

print(f"\nCOMPLETE: Retrieved {len(all_records)} records.")

for record in all_records[:1]:
    print(record)