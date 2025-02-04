from fastapi import FastAPI, Depends
import uvicorn
from routes.users import user_router
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from models.hero_model import Hero

app = FastAPI(
    title="FastAPI Auth", version="1.0.0", docs_url="/docs", redoc_url="/redocs"
)

app.include_router(user_router)

sqlite_file_name = "auth.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    Hero.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


sessionDep = Annotated[Session, Depends(get_session)]


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
