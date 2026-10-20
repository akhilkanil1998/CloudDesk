# imports the Fast Api package
from fastapi import FastAPI,Request
from app.api.v1.auth import auth_router
from app.api.v1.users import user_router
from app.core.logging_config import logger
from app.api.v1.tickets import ticket_router
import time
from contextlib import asynccontextmanager
# Import all models so SQLAlchemy registers them
import app.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("CloudDesk application startup initiated")

    # Startup initialization goes here

    logger.info("CloudDesk application startup completed")

    yield

    logger.info("CloudDesk application shutdown initiated")

    # Resource cleanup goes here

    logger.info("CloudDesk application shutdown completed")

# Instance of FastAPI
app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time) * 1000
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"{request.method}| {request.url.path}| status = {response.status_code}| duration = {process_time:.2f}")
    return response
    


# this will include the router in the auth file.
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ticket_router)
