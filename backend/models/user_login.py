from pydantic import BaseModel


class UserLogin(BaseModel):
    '''
    User login authentication
    @username: str
    @password: str
    '''
    username: str
    password: str