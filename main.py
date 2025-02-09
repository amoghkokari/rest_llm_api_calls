from fastapi import FastAPI
from generate_response import router as generate_response_router

# Initialize FastAPI application
fast_app = FastAPI()

# Include routers for different endpoints
fast_app.include_router(generate_response_router)