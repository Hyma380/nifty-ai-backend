from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "NIFTY AI Backend is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}