# imports the Fast Api package
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

# Import all models so SQLAlchemy registers them
import app.models
from app.api.v1.auth import auth_router
from app.api.v1.tickets import ticket_router
from app.api.v1.users import user_router
from app.core.logging_config import logger


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
    response = None
    try:
        response = await call_next(request)

    finally:
        process_time = (time.perf_counter() - start_time) * 1000

        if response is not None:
            response.headers["X-Process-Time"] = str(process_time)
            logger.info(
                f"{request.method}| {request.url.path}| status = {response.status_code}| duration = {process_time:.2f} ms"
            )

        else:
            logger.exception(
                f"{request.method} | {request.url.path} | "
                f"status=exception | duration={process_time:.2f} ms"
            )
    return response


# this will include the router in the auth file.
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ticket_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# for multiple file upload in swagger
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )

    # Use OpenAPI 3.0 format for Swagger file upload compatibility
    schema["openapi"] = "3.0.3"

    components = schema.get("components", {}).get("schemas", {})

    for component in components.values():
        properties = component.get("properties", {})

        for prop in properties.values():
            # Handle multiple file uploads
            items = prop.get("items", {})

            if items.get("contentMediaType") == "application/octet-stream":
                items.pop("contentMediaType")
                items["format"] = "binary"

            # Handle single file uploads
            if prop.get("contentMediaType") == "application/octet-stream":
                prop.pop("contentMediaType")
                prop["format"] = "binary"

    app.openapi_schema = schema
    return app.openapi_schema


app.openapi = custom_openapi
