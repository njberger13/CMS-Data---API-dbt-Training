import yaml

with open("/home/codespace/.dbt/profiles.yml", "r") as file:
    config = yaml.safe_load(file)

profile = config["healthcare_analytics_project"]["outputs"]["dev"]

print("Host:", profile["host"])
print("Port:", profile["port"])
print("Database:", profile["dbname"])
print("User:", profile["user"])
print("Password:", repr(profile["password"]))


from sqlalchemy import create_engine, text

connection_string = (
    f"postgresql+psycopg2://{profile['user']}:{profile['password']}"
    f"@{profile['host']}:{profile['port']}/{profile['dbname']}"
)

engine = create_engine(
    connection_string,
    connect_args={"sslmode": "require"}
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print(result.scalar())