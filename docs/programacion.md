# Configuración de desarrollo


## Desarrollo en local


### Docker compose
Podemos seleccionar varios perfiles en función de qué queramos probar.
| Perfil       | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `bd-sola`    | Utilizado únicamente para el servicio de `postgres`. Probablemente se usa para pruebas o desarrollo local cuando solo se necesita la base de datos sin otros servicios. |
| `backend`    | Incluye los servicios de `postgres` y `backend`. Utilizado para el desarrollo o pruebas donde el backend y la base de datos son necesarios. |
| `produccion` | Sirve para levantar todos los servicios. Incluye `postgres`, `backend`, y `frontend`. |
