from fastapi import FastAPI
from app.api.v1.endpoints import crud

app = FastAPI()

app.include_router(crud.router, prefix="/api")



