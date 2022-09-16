from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends, Response


from app.main.models.models import User
from app.main.config import settings
from app.main.infrastructure.database.db import get_db
from app.main.utility.utils import hash, verify
from app.main.helpers.jwt_handler import signJWT
from app.main.helpers.jwt_bearer import JWTBearer



from app.main.middlewares.role_checker import RoleChecker
from app.main.schemas.schemas import UserLoginSchema, UserSchema, UserCreateSchema,\
    TokenSchema, UserUpdateSchema, PasswordUpdateSchema




router = APIRouter(prefix='/user')
allow_view_resource = RoleChecker(["admin"])
allow_update_resource = RoleChecker(["admin", "subscriber"])

@router.post("/signup", status_code=status.HTTP_201_CREATED,
             response_model=UserSchema)
def user_signup(user: UserCreateSchema, db: Session = Depends(get_db)) -> dict:
    check_user = db.query(User).filter(User.email == user.email).first()
    if check_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with email already exist")
    hashed_password = hash(user.password)
    user.password = hashed_password

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=TokenSchema)
def user_login(response: Response, user: UserLoginSchema, db: Session = Depends(get_db)) -> dict:
    check_user = db.query(User).filter(
        User.email == user.email).first()

    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect email")

    if not verify(user.password, check_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password")

    access_token = signJWT(check_user.id, settings.JWT_EXPIRE_SECONDS)
    response.set_cookie(key="access_token",
                        value=f"{access_token}", expires=settings.JWT_EXPIRE_SECONDS, httponly=True, secure=True)

    return {"access_token": access_token}


@router.get('/get', response_model=List[UserSchema],
            dependencies=[Depends(allow_view_resource)])
def get_users(db: Session = Depends(get_db), limit: int = 10,
              skip: int = 0) -> List[dict]:
    users = db.query(User).limit(limit).offset(skip).all()
    return users


@router.get('/{id}', response_model=UserSchema,
            dependencies=[Depends(allow_view_resource)])
def get_one_user(id: str, db: Session = Depends(get_db)) -> dict:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str, db: Session = Depends(get_db),
                current_user: UserSchema = Depends(allow_update_resource)) -> dict:

    user_query = db.query(User).filter(User.id == id)

    user = user_query.first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")

    if current_user.role != "admin":
        if  id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not authorized to perform requested action")

    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=UserSchema)
def update_user(id: str, updated_post: UserUpdateSchema,
                db: Session = Depends(get_db),
                current_user: UserSchema = Depends(allow_update_resource)):

    user_query = db.query(User).filter(User.id == id)

    user = user_query.first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")

    if current_user.role != "admin":
        if  id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not authorized to perform requested action")
                                
    user_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return user_query.first()


@router.patch("/change_password/{id}", response_model=UserSchema)
def change_password(id: str, updated_user: PasswordUpdateSchema,
                    db: Session = Depends(get_db),
                    current_user: UserSchema = Depends(allow_update_resource)):

    user_query = db.query(User).filter(User.id == id)

    user = user_query.first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")

    if current_user.role != "admin":
        if  id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not authorized to perform requested action")

    if not verify(updated_user.old_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password")

    hashed_password = hash(updated_user.password)
    updated_user.password = hashed_password
    updated_user = updated_user.dict()
    updated_user.pop("old_password")
    user_query.update(updated_user, synchronize_session=False)

    db.commit()

    return user_query.first()