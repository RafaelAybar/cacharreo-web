from hashlib import sha3_512
from os import urandom

#https://pagorun.medium.com/password-encryption-in-python-securing-your-data-9e0045e039e1
def hash_contrasena(passw: str):
    sal = urandom(40)
    hash_passw = sha3_512()
    hash_passw.update(sal+ passw.encode())
    return hash_passw.hexdigest()