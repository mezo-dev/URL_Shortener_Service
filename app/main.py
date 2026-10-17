from fastapi import FastAPI

from app.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI(
    title="URL Shortener",
    version=0.1,
    description="A URL Shortener API Service that gives you a short version of your long URL.",
)


@app.get("/health")
def health_check():
    return {"status": "200-OK"}
