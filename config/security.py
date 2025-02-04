from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from models.user_model import User

security = HTTPBasic()


def verify_creds(user: User, credentials: HTTPBasicCredentials = Depends(security)):
    correct_name = user.name
    correct_password = user.password
    if credentials.username != correct_name or credentials.password != correct_password:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect name and pass",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
