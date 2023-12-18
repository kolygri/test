# Binance Stream Service

## Overview

This service connects to the Binance WebSocket stream and publishes the data to a Redis stream.

## Running Locally

1. Ensure you have Docker installed.
2. Build the Docker image: `docker build -t binance-stream-service .`
3. Run the Docker container: `docker run binance-stream-service`

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions to run tests and build the Docker image.
