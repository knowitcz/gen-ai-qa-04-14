import logging

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.api.account_routes import router as account_router
from app.api.bank_routes import router as bank_router
from app.api.client_routes import router as client_router
from app.api.transaction_routes import router as transaction_router
from app.db import engine
from app.logging_config import setup_logging
from app.models import Client, Transaction  # noqa: F401 - ensure tables are registered
from app.startup import create_default_accounts, create_default_clients

# Setup logging first
setup_logging()
logger = logging.getLogger(__name__)

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/assets", StaticFiles(directory="resources/web/dist/assets"), name="assets")

logger.info("Application starting up")

# Serve index.html from the static directory
@app.get("/")
def serve_static_files():
    return FileResponse("resources/web/dist/index.html")

app.include_router(account_router, prefix="/api/v1", tags=["account"])
app.include_router(bank_router, prefix="/api/v1", tags=["bank"])
app.include_router(client_router, prefix="/api/v1", tags=["client"])
app.include_router(transaction_router, prefix="/api/v1", tags=["transaction"])

# Catch-all route for client-side navigation — must be defined after API routers
# so it doesn't shadow them. Returns index.html for any unmatched path, allowing
# React Router to handle the route on the client side (e.g. refreshing /clients).
@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    return FileResponse("resources/web/dist/index.html")

create_default_clients()
create_default_accounts()
