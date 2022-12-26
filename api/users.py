from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from api.utils.users import get_user, get_user_by_email, get_users, create_user


router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users 

@router.post("/users")
async def create_new_user(user: User):
    users.append(user)
    return {'Success'}


@router.read("/users/{id}")
async def get_user(id: int):
    return {"user":users[id]}