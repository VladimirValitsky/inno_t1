import constants as const
from sqlalchemy import create_engine

# Params for DB
host = const.DB_HOST
dbname = const.DB_NAME
user = const.DB_USER_NAME
password = const.DB_PASS
port = const.DB_PORT
schema = const.DB_SCHEMA

# Connection to DB
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
print(f'Engine created successful ',{engine})


try:
    connection = engine.connect()
    print('Connection successful')

except Exception as connection_error:
    print(f'Error: during connection: {connection_error}')