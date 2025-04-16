
# FastAPI

A fun project with a simple implementation of DDD using FastAPI, designed to work as the backend for the Flutter DDD client. It follows Clean Architecture principles and aims to demonstrate good practices, domain separation, and scalability.

The backend connects to the public Binance API to fetch currency prices and also manages local favorites using a simple database layer.

This project is under development and is meant to showcase good practices, DDD, Clean Architecture, Design Patterns, and more.

### Docs
Docs are available with Swagger:
```
/docs # Swagger
/redocs # ReDoc
```

### Development Status  
🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ **90%** Architecture: DDD, implementing httpx  
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **100%** Binance API  
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ **00%** Favorites  
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ **00%** Automated Tests  
🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜ **50%** Documentation: automated Swagger  

### Initializing the Environemnt
source .venv/bin/activate

### Deactivating the Environment
deactivate

### Starting the App
uvicorn fastapi_ddd.main:app --reload --root-path .

### Update Requirements
pip freeze > requirements.txt