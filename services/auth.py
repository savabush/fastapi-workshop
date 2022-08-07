import datetime
from jose import jwt, JWTError
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from models.auth import User, UserCreate
from settings import settings, tables
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from models.auth import Token
from settings.database import get_session
from utils.exceptions import NotAuthorized


class AuthServices:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: UserCreate) -> Token:
        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password)
        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )
        if not user:
            raise NotAuthorized

        if not self.verify_password(password, user.password_hash):
            raise NotAuthorized

        return self.create_token(user)

    @classmethod
    def verify_password(cls, raw_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(raw_password, hashed_password)

    @classmethod
    def hash_password(cls, raw_password: str) -> str:
        return bcrypt.hash(raw_password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise NotAuthorized

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise NotAuthorized

        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)

        now = datetime.datetime.now()

        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + datetime.timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data.id)
        }

        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )

        return Token(access_token=token)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthServices.validate_token(token)
