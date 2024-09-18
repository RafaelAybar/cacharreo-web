from re import match
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm.session import Session
from .credenciales import hash_contrasena
from .db import User, conector_app


def valida_usuario(usuario: str) -> bool:
    return bool(match(r'^[a-zA-Z0-9]{5,20}$', usuario))


def valida_pass(contrasena: str) -> bool:
    return bool(match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$', contrasena))


def valida_cossy(cossy):
    return bool(match(r'^\d{10}$', cossy))

def conectordb ():
    db = Session(bind=conector_app)
    try:
        yield db # https://alvarohurtado.es/2020/06/08/que-hace-yield-en-python/
    finally:
        db.close()

app = FastAPI()


@app.get("/")
async def raiz():
    return {"mensaje": "Gestor de torneos"}


@app.get("/usuarios")
async def get_all_users():
    return "users"


@app.post("/crear_usuario")
async def creacion_usuario(usuario: str, passw: str, cossy_id: str, db: Session = Depends(conectordb)):
    if valida_cossy(cossy_id) and valida_usuario(usuario) and valida_pass(passw):
        usuario_existente = db.execute(select(User).filter_by(cossy=cossy_id)).scalars().first()
        if not usuario_existente:
            nuevo_usuario = User(usuario=usuario, cossy=cossy_id, contrasena=hash_contrasena(passw))
            db.add(nuevo_usuario)
            db.commit()
            return {"mensaje": "Usuario creado correctamente"}
        else:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    else:
        raise HTTPException(status_code=418, detail="Los datos no son válidos")