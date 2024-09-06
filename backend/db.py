from sqlalchemy import create_engine, MetaData, Table, Column, Integer, CheckConstraint, DateTime,func, Boolean, CheckConstraint
from sqlalchemy.dialects.postgresql import VARCHAR
import config


#engine = create_engine(f"postgresql+psycopg2://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}")
engine = create_engine(f"postgresql+psycopg2://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}")
metadata = MetaData()

users_table = Table('users', metadata,
                    Column('user_id', Integer, primary_key=True, autoincrement=True),
                    Column('username', VARCHAR(50), nullable=False, unique=True),
                    Column('email', VARCHAR(100), nullable=False, unique=True),
                    Column('password_hash', VARCHAR(255), nullable=False),
                    Column('first_name', VARCHAR(50)),
                    Column('last_name', VARCHAR(50)),
                    Column('created_at', DateTime(timezone=True), server_default=func.now()),
                    Column('updated_at', DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
                    Column('is_active', Boolean, default=True),
                    CheckConstraint(r"email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'", name='email_format')
                    )

# Create the table in the database
metadata.create_all(engine)

# Create the schema and the table in the database
metadata.create_all(engine)

print("Schema 'test' created successfully!")
