import redis
import logging

logger = logging.getLogger("fastapi-logger")


class RedisService:
    def __init__(self, url: str):
        self.client = redis.Redis.from_url(url)
        logger.info("Redis client initialized")

    def get_value(self, key: str):
        value = self.client.get(key)
        logger.info(f"Fetched value for key: {key}")
        return value

    def set_value(self, key: str, value: str):
        self.client.set(key, value)
        logger.info(f"Set value for key: {key}")
