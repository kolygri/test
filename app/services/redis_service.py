import json
import redis
import logging
from app.config.settigns import REDIS_HOST, REDIS_PORT, REDIS_DB

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
logger = logging.getLogger(__name__)


def publish_message(channel, message):
    try:
        r.publish(channel, json.dumps(message))
    except Exception as e:
        logger.error(f"Error publishing message to Redis: {e}")


def set_key_value(key, value):
    try:
        r.set(key, json.dumps(value))
    except Exception as e:
        logger.error(f"Error setting key-value in Redis: {e}")


def get_key_value(key):
    try:
        value = r.get(key)
        return json.loads(value) if value else None
    except Exception as e:
        logger.error(f"Error getting key-value from Redis: {e}")
        return None


def push_to_list(list_name, value):
    try:
        r.lpush(list_name, json.dumps(value))
    except Exception as e:
        logger.error(f"Error pushing to list in Redis: {e}")


def get_from_list(list_name, start=0, end=-1):
    try:
        elements = r.lrange(list_name, start, end)
        return [json.loads(element) for element in elements]
    except Exception as e:
        logger.error(f"Error getting from list in Redis: {e}")
        return []


def set_key_with_expiration(key, value, ttl):
    try:
        r.setex(key, ttl, json.dumps(value))
    except Exception as e:
        logger.error(f"Error setting key with expiration in Redis: {e}")
