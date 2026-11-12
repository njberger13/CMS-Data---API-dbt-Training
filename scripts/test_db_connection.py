
import yaml
import os

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Read dbt profile
with open("/home/codespace/.dbt/profiles.yml", "r") as file:
    config = yaml.safe_load(file)

profile = config["healthcare_analytics_project"]["outputs"]["dev"]

# Read password from Codespaces environment variable
password = os.environ["SUPABASE_DB_PASSWORD"]

print("Host:", profile["host"])
print("Port:", profile["port"])
print("Database:", profile["dbname"])
print("User:", profile["user"])
print("Password loaded:", bool(password))

# Build database connection
connection_url = URL.create(
    "postgresql+psycopg2",
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
