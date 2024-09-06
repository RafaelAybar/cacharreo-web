#!/usr/bin/python3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensaje": "Gestor de torneos"}
