from fastapi import FastAPI
from fastapi_ddd.presentation.example import example_router

app = FastAPI()

app.include_router(example_router.router, prefix="/api/v1")
