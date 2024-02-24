from datetime import datetime, timedelta
import os
import glob
from pathlib import Path

#TODO Fix placement 
def get_secret_path(filename : str) -> str:
    
    #get root path
    root_dir = "{}../../..".format(os.path.dirname(os.path.abspath(__file__)))
    root_dir = Path(root_dir).resolve()

    #get path
    result : list = glob.glob("{}/**/{}".format(root_dir, filename), recursive=True)

    return result[0]

import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import PyJWTError
from starlette.status import HTTP_403_FORBIDDEN
from app.core import config
import requests

ALGORITHM = "HS256"
access_token_jwt_subject = "access"

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not cred:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    try:
        cred = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={cred.credentials}")
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return cred.json()

    
