from fastapi import FastAPI
from app.free_tools import (
    youtube,
    instagram,
    tiktok,
    content_creation
)

# API TESTING: pytest app/free_tools/testing/test_api.py

app = FastAPI()
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
app.include_router(instagram.router, prefix="/instagram", tags=["Instagram"])
app.include_router(tiktok.router, prefix="/tiktok", tags=["Tiktok"])
app.include_router(content_creation.router, prefix="/content-creation", tags=["Content Creation"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}