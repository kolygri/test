import logging
import asyncio
from fastapi import FastAPI
from app.config.settigns import HOST, PORT
from app.routers import redis_router
from app.services.binance_consumer_service import consume_binance_stream

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI(
    title="Binance WebSocket stream consumer",
    description="Service consuming ticker data from Binance WebSocket stream",
    version="1.0.0",
    servers=[{"url": f"http://{HOST}:{PORT}"}],
)

app.include_router(redis_router.router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume_binance_stream())


@app.get("/")
async def read_root():
    return {"message": "Binance stream consumer is running"}
