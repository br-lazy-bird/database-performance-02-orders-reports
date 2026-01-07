from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.orders import router as orders_router
from app.core.logging_config import setup_logging

setup_logging()

app = FastAPI(
    title="Sales Reports API",
    description="Lazy Bird Project",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders_router)


@app.get("/")
async def root():
    """Root endpoint returning API status."""
    return {"message": "Sales Reports API is running"}


@app.get("/health")
async def health():
    """
    Health check endpoint.

    Returns:
        dict: Health status of the backend service.
    """
    return {"status": "healthy", "service": "backend"}