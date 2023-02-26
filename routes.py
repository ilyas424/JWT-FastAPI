from fastapi import Depends
from fastapi import HTTPException
from fastapi import APIRouter
from fastapi import APIRouter
from starlette.requests import Request
from sqlalchemy import exc


from schema import AuthDetails
from schema import AuthDetails_login
from sqlalchemy import exc

from auth import AuthHandler
import utils

auth_handler = AuthHandler()
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/users")
def read_item(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_user(session)
    return result


@router.post('/register', status_code=201)
def register(request: Request, user: AuthDetails):
    result = {}
    session = request.state.db   
    try:
        result = utils.post_create_user(session, user)
    except exc.IntegrityError:
        raise HTTPException(status_code=400, detail='пользователь с таким логином уже существует')
    return result


@router.post('/login')
def login(request: Request, auth_details: AuthDetails_login):
    result = {}
    session = request.state.db   
    result = utils.user_login(session, auth_details)
    if result == None:
            raise HTTPException(status_code=401, detail='Неверный пароль и/или логин ')
    if result.login == auth_details.login and auth_handler.verify_password(auth_details.hash, result.hash):
        token = auth_handler.encode_token(result.login)
        return { 'token': token }
        

@router.get("/users")
def read_item(request: Request):
    result = {}
    session = request.state.db
    result = utils.get_user(session)
    return result



@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'вход': username }