from re import match

from fastapi import FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm.session import Session
from backend.credenciales import hash_contrasena
from backend.db import User, conector_app


def valida_usuario(usuario: str) -> bool:
    return bool(match(r'^[a-zA-Z0-9]{5,20}$', usuario))


def valida_pass(contrasena: str) -> bool:
    return bool(match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$', contrasena))


def valida_cossy(cossy):
    return bool(match(r'^\d{10}$', cossy))


app = FastAPI()


@app.get("/")
async def raiz():
    return {"mensaje": "Gestor de torneos"}


@app.get("/usuarios")
async def get_all_users():
    return "users"


@app.post("/crear_usuario")
async def creacion_usuario(usuario: str, passw: str, cossy_id: str):
    if valida_cossy(cossy_id) and valida_cossy(usuario) and valida_pass(passw):
        with Session(bind=conector_app) as sesion:
            usuario_existente = select(User).filter_by(id=cossy_id)
            if not usuario_existente:
                nuevo_usuario = User(usuario=usuario, cossy=cossy_id, contrasena=hash_contrasena(passw))
                sesion.add(nuevo_usuario)
                sesion.commit()
                sesion.close()
                return {"mensaje": "Usuario creado correctamente"}
            else:
                sesion.close()
                raise HTTPException(status_code=400, detail="El usuario ya existe")
