from pydantic import BaseModel


class AuthDetails(BaseModel):
    login: str
    name: str
    hash: str

class AuthDetails_login(BaseModel):
    login: str
    hash: str