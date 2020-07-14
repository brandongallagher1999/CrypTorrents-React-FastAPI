import sys
sys.path.append("./database")
from database_api import Database_API
from models.user import User
from models.user_login import UserLogin
from password_hash import PasswordHash
from token_manager import TokenManager

class LoginManager():
    '''
    Manages login sessions for the given user.
    '''

    def __init__(self):
        self.database = Database_API()
        self.token_mg = TokenManager()
    
    def logout(self, user: User) -> None:
        '''
        Logs user out.

        @returns -> None.
        '''
        self.database.logout()

    def get_profile(self, token: str) -> User:
        '''
        Gets the user profile dictionary containing all public info like saved torrents, etc.

        :token: (str) encrypted JWT
        :return: (dict) user profile with saved torrents, and public updatable data
        '''
        try:
                
            token = bytes(token[2 : len(token)-1], encoding="utf-8")    #properly converting the cookie token string into bytes for decrypting

            unencrypted_token: str = self.token_mg.get_unencrypted_token(token) #unencrypt the given JWT
            temp_user_info: dict = self.token_mg.get_payload(unencrypted_token) #Get the JWT payload data (dictionary)

            userLogin_obj: UserLogin = UserLogin(username= temp_user_info["username"], password=temp_user_info["password"])

            user_obj: User = self.database.get_user(userLogin_obj) #Retrieve info from DB

            if (user_obj == None):
                return { "Message" : 401}
            
            else:
                return user_obj

        except:
            return None


    def create_session(self, user: UserLogin) -> bytes:
        '''
        Gets a user session token
        @returns: Token (str): token to be given to user accessing website (for their cookies)
        '''
        
        token: bytes = self.token_mg.get_encrypted_token(user)
        return token