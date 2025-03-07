from re import match
from sqlalchemy import select
from .db import User
from sqlalchemy.orm.session import Session


def valida_datos_para_registro(usuario: str, contrasena: str, cossy: str) -> bool:
    return (
        match(r"^[a-zA-Z0-9]{5,20}$", usuario)
        and match(
            r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$",
            contrasena,
        )
        and match(r"^\d{10}$", cossy)
    )


def valida_datos_para_login(cossy: str, contrasena: str) -> bool:
    return match(
        r"^\d{10}$",
        cossy
        and match(
            r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,15}$",
            contrasena,
        ),
    )


def usuario_existe(db: Session, cossy_id: str) -> User:
    return db.execute(select(User).filter_by(cossy=cossy_id)).scalars().first()
