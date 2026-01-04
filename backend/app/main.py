from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sales Reports API", description="Lazy Bird Project", version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Sales Reports API is running"}

@app.get("/health")
async def health():
    """
    Checks if the backend is running properly
    """
    return {"status": "healthy", "service": "backend"}