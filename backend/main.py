#!/usr/bin/python3

from fastapi import FastApi
app = FastApi()

@app.get("/")
async def raiz():
    return {"message": "Gestor de torneos"}