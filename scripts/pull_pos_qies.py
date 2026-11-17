import requests
import time
from sqlalchemy import text, bindparam
from sqlalchemy.dialects.postgresql import JSONB
from scripts.db_connection import get_engine


# CMS POS/QIES API endpoint
url = "https://data.cms.gov/data-api/v1/dataset/8ba0f9b4-9493-4aa0-9f82-44ea9468d1b5/data"


def extract_pos_qies():

    batch_size = 5000
    offset = 0
    all_records = []

    while True:

        # Define API request parameters
        params = {
            "size": batch_size,
            "offset": offset
        }

        # Send request to CMS
        response = requests.get(url, params=params, timeout=60)

        # Check for HTTP errors
        response.raise_for_status()

        # Convert JSON response into Python objects
        batch = response.json()

        # Add records to our collection
        all_records.extend(batch)

        print(f"Retrieved {len(batch)} records. Total: {len(all_records)}")

        # Stop when there are no more records
        if len(batch) < batch_size:
            break

        # Move to the next batch
        offset += len(batch)

    return all_records






def load_pos_qies(records):

    engine = get_engine()

    with engine.begin() as connection:

        step_start = time.perf_counter()

        # Create table if it doesn't already exist
        # "generated always as identity primary key" auto assigns a unique sequential ID to each row
        # JSONB not null --> ignores null entries
        # "raw." is the schema
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS raw.pos_qies (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
                data JSONB NOT NULL
            );
        """))

        print(f"Table creation/check: {time.perf_counter() - step_start:.2f} seconds", flush=True)

        step_start = time.perf_counter()

        # First, remove existing records and reset the ID sequence
        connection.execute(
            text("TRUNCATE TABLE raw.pos_qies RESTART IDENTITY;")
        )

        # Insert provider records
        # inserts the data 
        connection.execute(
            text("""
                INSERT INTO raw.pos_qies (data)
                VALUES (:data)
            """).bindparams(
                bindparam("data", type_=JSONB)
                ),
            [{"data": record} for record in records] #[0:1000]] #only testing a subset of the data for now
        )

    print(f"Successfully loaded {len(records)} records.")


# only runs if the file is run by itself, not imported
if __name__ == "__main__":

    start_time = time.perf_counter()

    print("Starting CMS data extraction for POS QIES...", flush=True)
    records = extract_pos_qies()

    extraction_time = time.perf_counter() - start_time
    print(f"Extraction complete: {len(records)} records in {extraction_time:.2f} seconds.", flush=True)

    load_start = time.perf_counter()

    print("Starting database load...", flush=True)
    load_pos_qies(records)

    load_time = time.perf_counter() - load_start
    print(f"Database load complete in {load_time:.2f} seconds.", flush=True)

    total_time = time.perf_counter() - start_time
    print(f"Total pipeline runtime: {total_time:.2f} seconds.", flush=True)
