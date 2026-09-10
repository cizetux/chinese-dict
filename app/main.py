from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router

app = FastAPI(title="Chinese → English Dictionary")

# Crée la DB au démarrage
Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "API is running"}
