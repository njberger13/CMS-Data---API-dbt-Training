
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

print("Host:", profile["host"])
print("Port:", profile["port"])
print("Database:", profile["dbname"])
print("User:", profile["user"])
print("Password loaded:", bool(password))

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

#once the function is defined in scripts folder, all the above can be replaced with line below
#engine = get_engine()

# Test connection
with engine.connect() as connection:
    result = connection.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
    connection.commit()
    print("Raw schema created successfully!")