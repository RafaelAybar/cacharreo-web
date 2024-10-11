from os import getenv

POSTGRES_DB=getenv("POSTGRES_DB", "test")
POSTGRES_HOST=getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT=getenv("POSTGRES_PORT", 5432)
POSTGRES_SCHEMA=getenv("POSTGRES_SCHEMA", "gestor_torneos")

APP_DB_USER=getenv("APP_DB_USER", "admin_aplicacion")
APP_DB_PASS=getenv("APP_DB_PASS", "securepassowrd")

CLAVE_SECRETA=getenv("CLAVE_SECRETA", "Cámbiame inmediatamente") # Para firmar las cookies