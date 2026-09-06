from contextlib import asynccontextmanager

import uvicorn
import logging
from fastapi import FastAPI, logger

from .config import settings
from .routers import commands

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"starting up app on {settings.host}:{settings.port}")
    
    yield
    
    logger.info("shutting down app")
    

app = FastAPI(lifespan=lifespan)

app.include_router(commands.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )