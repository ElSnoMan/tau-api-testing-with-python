from typing import List
from pydantic import BaseModel


class BookModel(BaseModel):
    isbn: str
    title: str
    subTitle: str
    author: str
    publish_date: str
    publisher: str
    pages: int
    description: str
    website: str


class UserModel(BaseModel):
    userID: str
    username: str
    books: List[BookModel]


class TokenModel(BaseModel):
    token: str
    expires: str
    status: str
    result: str
