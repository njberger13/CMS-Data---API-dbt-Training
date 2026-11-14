
import yaml
import os #to grab secret password

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Read dbt profile; "r" is read mode
with open("/home/codespace/.dbt/profiles.yml", "r") as file:
    config = yaml.safe_load(file)

profile = config["healthcare_analytics_project"]["outputs"]["dev"]

# Read password from Codespaces environment variable
password = os.environ["SUPABASE_DB_PASSWORD"]

# Build database connection with SQLAlchemy functions below
connection_url = URL.create(
    "postgresql+psycopg2", #type of database + driver
    username=profile["user"],
    password=password,
    host=profile["host"],
    port=int(profile["port"]),
    database=profile["dbname"],
    query={"sslmode": "require"}
)

engine = create_engine(connection_url)

# Test connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("Connection successful!")
    print(result.scalar())
