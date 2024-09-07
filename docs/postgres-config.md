# Configuración de Postgres
1. Variables de enorno para arrancar la base de datos.

En la carpeta env, hay que crear el fichero `postgres.env`, y poner las variables de la siguiente manera:
```
POSTGRES_USER=test
POSTGRES_PASS=test
POSTGRES_DB=test
```
Cambia los valores por defecto.

2. Crea las variables de entorno para que la app cree el Schema de la base de datos.

Ejemplo:

```
POSTGRES_DB=test
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
APP_DB_USER=admin_aplicacion
APP_DB_PASS=CámbiamePorFavor2024
```
Dentro de docker, en lugar de localhost, deberá ser `POSTGRES_HOST=postgres`, puesto que docker "traduce" el nombre de servicio de la base de datos

3. Crea el usuario de postgres de la propia app.

Esto es debido a que con usuario con todos de los permisos de postgres no debemos ejecutar la aplicación.
Por ello vamos a crear un usuario nuevo que sólo tenga permisos en nuestra base de datos nueva, y esto ya depende de cómo se plantee el diseño de la base de datos.

El código en SQL podría ser este:
```SQL
CREATE user admin_aplicacion WITH PASSWORD 'CámbiamePorFavor2024';

-- Permisos al nivel de schema
GRANT CONNECT ON DATABASE test TO admin_aplicacion;
GRANT USAGE ON SCHEMA gestor_torneos TO admin_aplicacion;
GRANT CREATE ON SCHEMA gestor_torneos TO admin_aplicacion;

--Permisos para todas las tablas del schema
GRANT SELECT, UPDATE ON ALL TABLES IN SCHEMA gestor_torneos TO admin_aplicacion;

-- Mismos privilegios para tablas nuevas
ALTER DEFAULT PRIVILEGES IN SCHEMA gestor_torneos GRANT SELECT, UPDATE ON TABLES TO admin_aplicacion;
```