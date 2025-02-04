from fastapi import FastAPI
import uvicorn
from routes.users import user_router
from config.db_config import create_db_and_tables

app = FastAPI(
    title="FastAPI Auth", version="1.0.0", docs_url="/docs", redoc_url="/redocs"
)

app.include_router(user_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
