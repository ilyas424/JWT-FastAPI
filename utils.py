from sqlalchemy.orm import Session

from models import User
from schema import AuthDetails
from schema import AuthDetails_login

from auth import AuthHandler

auth_handler = AuthHandler()

def get_user(session: Session):
    return session.query(User).all()



def post_create_user(session: Session, user: AuthDetails ):
    hashed_password = auth_handler.get_password_hash(user.hash)
    x = user.dict()
    x['hash'] = hashed_password
    post = User(**x)
    session.add(post)
    session.commit()
    return post


def user_login(session: Session, user: AuthDetails_login):
    return session.query(User).filter(User.login == user.login).first()
