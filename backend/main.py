from fastapi import FastAPI

app = FastAPI(title="Personal Knowledge Vault")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/")
def root():
    return {"message": "PKV API is running"}