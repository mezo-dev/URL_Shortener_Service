from fastapi import FastAPI

from app.database import Base, engine
from routers.urls import router as urls_router

Base.metadata.create_all(engine)

app = FastAPI(
    title="URL Shortener",
    version="0.1",
    description="Shorten long URLs and redirect visitors to the original.",
)

app.include_router(urls_router)


@app.get("/health")
def health_check():
    return {"status": "200-OK"}
