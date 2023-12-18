import asyncio
import websockets
import json

async def consume_binance_stream():
    uri = "wss://stream.binance.com:9443/ws/bnbbtc@ticker"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            # Process and publish to another stream (e.g., Redis pubsub)
            # Example: print(data)

async def main():
    await consume_binance_stream()

if __name__ == "__main__":
    asyncio.run(main())
