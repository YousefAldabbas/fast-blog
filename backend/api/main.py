
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .config import engine,Base
from .routers import routers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="fast-blog"
)
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers)


