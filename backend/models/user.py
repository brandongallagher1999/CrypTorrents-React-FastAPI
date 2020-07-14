from datetime import date
from pydantic import BaseModel
from .torrent import Torrent
from typing import List

class User(BaseModel):
    '''
    User stored in the database (not for authentication.)
    '''
    username: str
    saved_torrents: List[Torrent]
    logged_in: bool