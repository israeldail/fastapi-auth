from fastapi import Depends
from typing import Annotated
from sqlmodel import Session, create_engine
from models.user_model import User

sqlite_file_name = "auth.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    User.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


sessionDep = Annotated[Session, Depends(get_session)]
