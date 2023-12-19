import uvicorn
from fastapi import FastAPI
import asyncio
import json
import websockets
import redis_service

app = FastAPI()


async def consume_binance_stream():
    uri = "wss://stream.binance.com:9443/ws/bnbbtc@ticker"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    message = await websocket.recv()
                    try:
                        data = json.loads(message)
                        try:
                            redis_service.publish_message("bnb_btc_stream", data)
                        except Exception as e:
                            print(f"Error publishing message to Redis: {e}")
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                except Exception as e:
                    print(f"Error receiving WebSocket message: {e}")
                    # Optionally, add a break or reconnection logic here
    except Exception as e:
        print(f"Error connecting to WebSocket: {e}")
        # Reconnection logic can be added here if desired

def start_consume_binance_stream():
    asyncio.create_task(consume_binance_stream())

@app.get("/")
async def read_root():
    return {"message": "Binance stream consumer is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
