from re import match
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm.session import Session
from .credenciales import hash_contrasena, comprobar_contrasena
from .db import User, conector_app


def valida_datos(usuario: str, contrasena: str , cossy: str) -> bool:
    return match(r'^[a-zA-Z0-9]{5,20}$', usuario) and match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$', contrasena) and  match(r'^\d{10}$', cossy)


def conectordb ():
    db = Session(bind=conector_app)
    try:
        yield db # https://alvarohurtado.es/2020/06/08/que-hace-yield-en-python/
    finally:
        db.close()

def usuario_existe(db: Session, cossy_id: str) -> User:
    usuario_existente = db.execute(select(User).filter_by(cossy=cossy_id)).scalars().first()
    return usuario_existente

app = FastAPI()


@app.get("/")
async def raiz():
    return {"mensaje": "Gestor de torneos"}


@app.get("/usuarios")
async def get_all_users():
    return "users"


@app.post("/crear_usuario")
async def creacion_usuario(usuario: str, passw: str, cossy_id: str, db: Session = Depends(conectordb)):
    if valida_datos(usuario, passw, cossy_id):
        if not usuario_existe(db, cossy_id):
            nuevo_usuario = User(usuario=usuario, cossy=cossy_id, contrasena=hash_contrasena(passw))
            db.add(nuevo_usuario)
            db.commit()
            return {"mensaje": "Usuario creado correctamente"}
        else:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    else:
        raise HTTPException(status_code=418, detail="Los datos no son válidos")


@app.post("/login")
async def login(usuario: str, passw: str, cossy_id: str, db: Session = Depends(conectordb)):
  if valida_datos(usuario, passw, cossy_id):
    usuario_existente = usuario_existe(db, cossy_id)
    if usuario_existente:
            hash_almacenado = usuario_existente.contrasena
            if comprobar_contrasena(passw, hash_almacenado):
                return {"mensaje": "¡Sesión iniciada!"}
            else:
                return {"mensaje":"Cossy o contraseña inválidos"}
    else:
        return {"mensaje": "El usuario no existe"}
  else:
    return {"mensaje": "Datos no válidos"}
