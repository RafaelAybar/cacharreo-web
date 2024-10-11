from hashlib import scrypt
from os import urandom
from fastapi.security import
def hash_contrasena(contrasena: str):
    sal = urandom(25)
    hash_contrasena = scrypt(contrasena.encode(), salt=sal, n=16384, r=8, p=1)
    return sal + hash_contrasena


def comprobar_contrasena(contrasena: str, hash_almacenado: bytes) -> bool:
    sal_almacenada = hash_almacenado[:25]
    clave_almacenada = hash_almacenado[25:]
    nuevo_hash = scrypt(contrasena.encode(), salt=sal_almacenada, n=16384, r=8, p=1)
    return nuevo_hash == clave_almacenada
