from typing import Annotated
from fastapi import APIRouter, Query
from sqlmodel import select
from models.user_model import User
from config.db_config import sessionDep

user_router = APIRouter()


@user_router.get("/users", response_model=list[User])
def read_users(
    session: sessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@user_router.post("/users")
def create_user(user: User, session: sessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
