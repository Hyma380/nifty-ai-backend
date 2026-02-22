from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NIFTY AI Backend is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}