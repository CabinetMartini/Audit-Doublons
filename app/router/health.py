from fastapi import APIRouter  # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

health = APIRouter()


# Route de santé pour vérifier le service
@health.get("/health", status_code=200)
async def health_check():
    """Route de vérification de santé du service"""
    return {
        "status": "healthy",
        "service": f"{os.getenv("APP_CONFIG_TITLE")}",
    }