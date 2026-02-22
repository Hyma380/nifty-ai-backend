from fastapi import FastAPI
from database import engine
from models import Trade
from database import Base
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
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Trade

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/trade")
def create_trade(symbol: str, side: str, quantity: float, price: float, db: Session = Depends(get_db)):
    trade = Trade(symbol=symbol, side=side, quantity=quantity, price=price)
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
