from fastapi import FastAPI
from pydantic import BaseModel
from videoclub_api import VideoClub

app = FastAPI()

@app.get('/listarpeliculas')
def listar_peliculas():
    db = VideoClub()
    return db.mostrar_peliculas()

@app.get('/mostrar_istorial')
def mostrar_istorial():
    db = VideoClub()
    return db.mostrar_historial()


