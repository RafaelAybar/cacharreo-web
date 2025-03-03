from hashlib import scrypt
from os import urandom
from jwt import encode
from jwt.exceptions import InvalidTokenError
import datetime
from config import CLAVE_SECRETA


def hash_contrasena(contrasena: str):
    sal = urandom(25)
    hash_contrasena = scrypt(contrasena.encode(), salt=sal, n=16384, r=8, p=1)
    return sal + hash_contrasena


def comprobar_contrasena(contrasena: str, hash_almacenado: bytes) -> bool:
    sal_almacenada = hash_almacenado[:25]
    clave_almacenada = hash_almacenado[25:]
    nuevo_hash = scrypt(contrasena.encode(), salt=sal_almacenada, n=16384, r=8, p=1)
    return nuevo_hash == clave_almacenada


def generar_jwt(clave: str, tiempo_expira_horas: int, cossy: str) -> str:
    payload = {"cossy": cossy, "fecha": datetime.datetime.now(datetime.UTC)}

    algoritmo = "HS256"
    token = encode(payload, CLAVE_SECRETA, algorithm=algoritmo)
    return token
