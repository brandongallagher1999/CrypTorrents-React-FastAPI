import sqlite3
import hashlib
import sys
sys.path.append("..")
from password_hash import PasswordHash
from models.user import User
from models.torrent import Torrent
from models.user_login import UserLogin
from typing import List

class Database_API():
    '''
    Interacts with the SqlLite3 database through sqllite3 library.

    :returns: None
    '''
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.c = self.connection.cursor()

    def create_table(self) -> None:
        self.c.execute('''
            CREATE TABLE user(
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                primary key(username)
            )
        ''')

    def get_user(self, user: UserLogin) -> User:
        '''
        Gets a single user based on their login info

        @returns: User -> a single user
        '''

        temp_user: User = User()
        if (self.user_exists(user)):    #Check to see if the user actually exists in the database with proper user/password.
            
            #User model contains relevant user information, part 1 of joining the user info and saved_torrents info
            for row in self.c.execute('''
                SELECT username, logged_in
                FROM user
                WHERE username = {}
            '''.format(user.username)):
                temp_user.username = row[0]
                temp_user.logged_in = row[2]
            
            #All the torrents that this user has saved.
            for row in self.c.execute('''
                SELECT * from 'torrent'
                WHERE user_id = {}
            '''.format(user.username)):
                temp_user.saved_torrents.append(Torrent(name=row[0], magnet=row[1], size=row[2], category=row[3])) #Append to User Model's list of torrents.

            return temp_user

        else:   #if they don't exist, return None
            return None
            

    def get_users(self) -> List[User]:
        '''
        Gets all users from the database except their passwords.

        @Returns: List[User] -> All users without password.
        '''
        users: List[User] = []
        for row in self.c.execute("SELECT username, saved_torrents, logged_in FROM users"):
            temp = User()
            temp.username = row[0]
            temp.password = ""
            temp.saved_torrents = row[1]
            temp.logged_in = row[2]
            users.append(User)  #Append temp object to the list
        
        return users
    
    def user_exists(self, user: UserLogin):
        count: int = 0
        hashed_passw = PasswordHash(user.password)

        for row in self.c.execute('''
            SELECT * from user WHERE username = '{}' AND password = {}
        '''.format(user.username, hashed_passw)):
           count += 1
        
        if (count == 1):
            return True
        else: 
            return False
    
    def set_logstatus(self, status: str, username: str) -> None:
        self.c.execute('''
            UPDATE user
            SET logged_in = {}
            WHERE username = {}
        '''.format(status, username))

    def set_logout(self, user: User) -> None:
        self.set_logstatus("FALSE", user.username)
    
    def set_login(self, user: User) -> None:
        self.set_logstatus("TRUE", user.username)
    
    def check_username_exists(self, user: User) -> bool:

        count: int = 0

        for row in self.c.execute('''
            SELECT * from user WHERE username = '{}'
        '''.format(user.username)):
           count += 1
        
        # See if at least one row exists if not then return false
        if (count > 0):
            return True
        else:
            return False


    #def logout(self, user: User) -> None:
        
    def add_user(self, username: str, passw: str):
        '''
        Inserts a new user into the user table.

        @username: str -> Username of the user
        @passw: str -> Password of the user

        @returns -> None
        '''

        if (self.check_username_exists(username) == False): #If the user doesn't exist, then add them
            self.c.execute('''
                INSERT INTO user VALUES (
                    '{}',
                    '{}'
                )
            '''.format(username, PasswordHash(passw)))  #Add the username, and a salted --> hashed password.
        
        #Save the database changes
        self.connection.commit()

    def close_db(self):
        self.connection.close()