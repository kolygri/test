import os

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 8000)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)
STREAM_URI = os.getenv("STREAM_URI", "wss://stream.binance.com:9443/ws/bnbbtc@ticker")
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL", "bnb_btc_stream")
