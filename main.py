from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NIFTY AI Backend is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

from fastapi import FastAPI
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Trading Backend Running"}