from datetime import datetime, timezone
from sqlalchemy import create_engine, Column, String, DateTime, LargeBinary
from sqlalchemy.orm import DeclarativeBase
from .config import APP_DB_USER, APP_DB_PASS, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST, POSTGRES_SCHEMA

conector_app = create_engine(
    f"postgresql+psycopg2://{APP_DB_USER}:{APP_DB_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': POSTGRES_SCHEMA}
    cossy = Column(String(10), primary_key=True)
    usuario = Column(String(15), unique=True, nullable=False)
    contrasena = Column(LargeBinary, nullable=False)
    created = Column(DateTime, default=datetime.now(timezone.utc).replace(tzinfo=None))
    last_login = Column(DateTime, nullable=True)


Base.metadata.create_all(conector_app)
