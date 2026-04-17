import time
import redis
import logging
from fastapi import HTTPException
from .config import settings

logger = logging.getLogger(__name__)

# Initialize Redis connection
if settings.redis_url:
    r = redis.from_url(settings.redis_url)
else:
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def check_rate_limit(key: str):
    """
    Check rate limit using Redis.
    Will raise HTTPException 429 if the limit is exceeded.
    """
    now = int(time.time())
    window_key = f"rate_limit:{key}:{now // 60}"
    
    try:
        current_count = r.incr(window_key)
        if current_count == 1:
            r.expire(window_key, 60)
        
        if current_count > settings.rate_limit_per_minute:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded: {settings.rate_limit_per_minute} req/min",
                headers={"Retry-After": "60"},
            )
    except redis.exceptions.ConnectionError:
        logger.warning("Redis is not available, bypassing rate limit check.")
