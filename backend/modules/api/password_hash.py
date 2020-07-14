import hashlib

class PasswordHash():
    '''
    Salts and hashes a given password
    @returns -> str: a salted and hashed password.
    '''

    def __init__(self, password: str):
        self.password = password
        self.salt = "f54ga"

    def hash(self) -> str:
        '''
        @returns -> str: Hashed password
        '''
        return hashlib.md5(str(f"{self.salt}{self.password}{self.salt}").encode("utf-8")).hexdigest()

    def __str__(self) -> str:
        '''
        Allows for p = PasswordHash("password") to auto return the hashed value
        '''
        return self.hash()