
import os
import yaml

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def get_engine():

    # Locate and read the dbt profile
    profile_path = Path.home() / ".dbt" / "profiles.yml"

    with open(profile_path, "r") as file:
        config = yaml.safe_load(file)

    # Extract database configuration
    profile = config["healthcare_analytics_project"]["outputs"]["dev"]

    # Retrieve database password
    password = os.environ["SUPABASE_DB_PASSWORD"]

    # Construct database connection URL
    connection_url = URL.create(
        "postgresql+psycopg2",
        username=profile["user"],
        password=password,
        host=profile["host"],
        port=int(profile["port"]),
        database=profile["dbname"],
        query={"sslmode": "require"}
    )

    # Create and return SQLAlchemy engine
    engine = create_engine(connection_url)

    return engine
