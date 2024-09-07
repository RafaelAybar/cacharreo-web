from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime, timezone

import config

# Evitamos
coneector_app = create_engine(f"postgresql+psycopg2://{config.APP_DB_USER}:{config.APP_DB_PASS}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'usuarios'
    __table_args__= { 'schema': config.POSTGRES_SCHEMA }
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.now(timezone.utc).replace(tzinfo=None))
    last_login = Column(DateTime, nullable=True)


Base.metadata.create_all(coneector_app)

print("Todo creado en orden")
