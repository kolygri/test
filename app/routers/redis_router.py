from app.config.settigns import REDIS_CHANNEL
from app.services.binance_consumer_service import META_BINANCE_SERVICE
from fastapi import APIRouter

router = APIRouter(tags=["redis-stream"])


@router.get("/default-redis-channel")
async def get_default_channel():
    """Endpoint to get the default Redis channel."""
    return {"default_channel": REDIS_CHANNEL}


@router.get("/message-count")
async def get_message_count():
    """Endpoint to get the total count of messages."""
    return {"message_count": META_BINANCE_SERVICE.message_count}
