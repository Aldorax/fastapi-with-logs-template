from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import logging
import time

logger = logging.getLogger("fastapi-logger")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_start_time = time.time()

        logger.info(f"Request: {request.method} {request.url}")
        logger.info(f"Headers: {request.headers}")
        logger.info(f"Client: {request.client.host}")

        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(f"Exception: {str(e)}")
            response = JSONResponse(
                content={"detail": "Internal Server Error"}, status_code=500)

        process_time = time.time() - request_start_time
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Process Time: {process_time} seconds")

        return response
