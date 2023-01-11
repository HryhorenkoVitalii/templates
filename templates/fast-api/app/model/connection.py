from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from config import DatabaseConfig as config

connection_url = URL.create(
    "postgresql+psycopg2",
    username=config.username,
    password=config.password,
    host=config.host,
    database=config.database,
)


engine = create_engine(
    connection_url,
    encoding='utf8',
    future=True,
)

Session = sessionmaker(bind=engine, future=True)

metadata = MetaData()
