import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def publish_message(message):
    r.publish('binance_stream', message)
