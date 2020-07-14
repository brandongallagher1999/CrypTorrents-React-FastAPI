
#from ..config.config_manager import ConfigManager
import jwt
import datetime
from models.user_login import UserLogin
from config_manager import ConfigManager
from cryptography.fernet import Fernet

class TokenManager():
    '''
    Manages JSON web tokens and gives a token response back based on given user
    '''

    def __init__(self):
        
        self.config = ConfigManager()
        self.key = Fernet.generate_key()
        #self.config.set_crypto(self.key)
        self.frn: Fernet = Fernet(self.config.get_crypto())

    def get_unencrypted_token(self, t: bytes) -> bytes:
        '''
        Unencrypts the given JWT

        @token: (bytes)-> JWT Token
        @returns: (bytes) -> A encrypted token.
        '''

        return self.frn.decrypt(t)

    def get_encrypted_token(self, user: UserLogin) -> bytes:
        '''
        Gives a JWT response encoded.

        @user: UserLogin -> username and password from the login form in front end
        @returns: str -> A JWT token
        '''

        token: str = jwt.encode(    #This token is to be given to the user
            {
                "username" : user.username,
                "password" : user.password,
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(days=1)
            },
            self.config.get_config("secret"),
            algorithm="HS256"
        )

        return self.frn.encrypt(token)  #encrypting the login JWT

    def get_payload(self, token: bytes) -> dict:
        '''
        Gets the payload data from a given token, decoded using a secret.

        @token: str -> the JWT
        @returns: dict -> The user's information.
        '''

        payload: dict = jwt.decode(
            token,
            self.config.get_config("secret"),
            algorithms=["HS256"]
        )
        return payload