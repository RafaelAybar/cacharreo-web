#!/usr/bin/python3
from fastapi import FastAPI
from re import match
from sqlalchemy import select
from sqlalchemy.orm.session import Session
from db import coneector_app, User

def valida_usuario(usuario: str) -> bool:
    return bool(match(r'^[a-zA-Z0-9]{5,20}$', usuario))

def valida_pass(contrasena: str)-> bool:
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

@app.post("crear_usuario")
async def creacion_usuario(user:str, passw:str , cossy_id: str) -> str:
    mensaje = "Usuario creado con éxito"
    if valida_cossy(cossy_id) and valida_cossy(usuario) and valida_pass(passw):
        with Session(bind=coneector_app) as sesion:
            usuario_existente = select(User).filter_by(id=cossy_id)
            if not usuario_existente:
                usuario = User(usuario=user, cossy=cossy_id, contrasena=passw),
            else:
                mensaje = "El usuario con ese cossy ya existe"
    return mensaje