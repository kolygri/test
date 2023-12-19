import logging
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def publish_message(channel, message):
    try:
        r.publish(channel, json.dumps(message))
    except Exception as e:
        logger.error(f"Error publishing message to Redis: {e}")
