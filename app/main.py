from fastapi import FastAPI
from fastapi.responses import FileResponse
from sqlmodel import SQLModel
from app.db import engine
from app.api.account_routes import router as account_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

# Serve index.html from the static directory
@app.get("/")
def serve_static_files():
    return FileResponse("resources/static/index.html")

app.include_router(account_router, prefix="/api/v1", tags=["account"])

create_default_accounts()