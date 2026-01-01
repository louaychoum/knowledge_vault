from fastapi import FastAPI
from routes.notes import router as notes_router

app = FastAPI(title="Personal Knowledge Vault")

app.include_router(notes_router)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/")
def root():
    return {"message": "PKV API is running"}