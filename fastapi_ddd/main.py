from fastapi import FastAPI
# from fastapi_ddd.presentation.favorites import favorites_router
from fastapi_ddd.presentation.quotes import quotes_router

app = FastAPI()

# app.include_router(favorites_router.router, prefix="/api/v1")
app.include_router(quotes_router.router, prefix="/api/v1")
