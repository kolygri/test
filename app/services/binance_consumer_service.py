import json
import websockets
import logging
from threading import Lock
from app.config.settigns import STREAM_URI, REDIS_CHANNEL
import app.services.redis_service as redis_service

logger = logging.getLogger(__name__)


class MetaBinanceService:
    def __init__(self):
        self.message_count = 0
        self.lock = Lock()

    def increment_message_count(self):
        with self.lock:
            self.message_count += 1

    def reset_message_count(self):
        with self.lock:
            self.message_count = 0

    def get_message_count(self):
        with self.lock:
            return self.message_count


META_BINANCE_SERVICE = MetaBinanceService()


async def consume_binance_stream():
    try:
        async with websockets.connect(STREAM_URI) as websocket:
            while True:
                try:
                    message = await websocket.recv()
                    try:
                        data = json.loads(message)
                        try:
                            redis_service.publish_message(REDIS_CHANNEL, data)
                            META_BINANCE_SERVICE.increment_message_count()
                        except Exception as e:
                            logger.error(f"Error publishing message to Redis: {e}")
                    except json.JSONDecodeError as e:
                        logger.error(f"Error decoding JSON: {e}")
                except Exception as e:
                    logger.error(f"Error receiving WebSocket message: {e}")
                    # Optionally, add a break or reconnection logic here
    except Exception as e:
        logger.error(f"Error connecting to WebSocket: {e}")
        # Reconnection logic can be added here if desired
