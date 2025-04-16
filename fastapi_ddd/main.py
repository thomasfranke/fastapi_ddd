from fastapi import FastAPI
from fastapi_ddd.presentation.quotes import quotes_router

app = FastAPI()

app.include_router(quotes_router.router, prefix="/api/v1")
