# Binance Stream Service

## Overview

This service connects to the Binance WebSocket stream and publishes the data to a Redis stream.

## Running Container

1. Ensure you have Docker installed.
2. Build the Docker image: `docker build -t binance-stream-service .`
 * In the case you want to forece a docker rebuild use `docker build --no-cache -t binance-stream-service .`
3. Run the Docker container: `docker run binance-stream-service`
4. Log in the container interactively: `docker exec -it <container-id> /bin/bash` and execute `curl http://0.0.0.0:8000/` to test the service.

## Running Locally
Note: You will need to have Redis running locally.

1. Run the command `poetry run python run.py` to start the service. Navigate to `http://0.0.0.0:8000/` to test the service.
2. Check that messages are being published to the Redis stream, run the command `redis-cli` on the command line and then `SUBSCRIBE bnb_btc_stream` to subscribe to the stream.
3. You can hit endpoints such as `http://0.0.0.0:8000/default-redis-channel` and `http://0.0.0.0:8000/message-count` to get some metadata about the stream.

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions to run tests and build the Docker image.
