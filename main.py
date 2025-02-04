from fastapi import FastAPI
import uvicorn
from routes.users import user_router

app = FastAPI(
    title="FastAPI Auth", version="1.0.0", docs_url="/docs", redoc_url="/redocs"
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
