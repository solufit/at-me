from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "postgresql+psycopg2://postgre:postgre@db:5432/atme"
)
session = sessionmaker(
    engine = engine,
    autoflush=True
)
