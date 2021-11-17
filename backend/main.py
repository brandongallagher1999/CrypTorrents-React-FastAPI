import sys
from starlette.middleware.cors import CORSMiddleware
import json
import os
from starlette.requests import Request
from fastapi import FastAPI, Body
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette import responses
sys.path.append("./modules/database/")
sys.path.append("./modules/api/")
sys.path.append("./modules/config/")
from database_api import Database_API
from pirate_api import Pirate_API
from login_manager import LoginManager
from models.user_login import UserLogin
from models.user import User
from starlette import responses
from fastapi.encoders import jsonable_encoder
import sqlite3



app = FastAPI()
pirate_api = Pirate_API()
database = Database_API()

origins = ["http://localhost:3000"]

# TODO: Change origin to real domain to reject Ajax requests from elsewhere
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])



@app.get("/api/torrents/")
async def get_torrent(request: Request, torrent: str = "") -> responses.JSONResponse:
    '''
    Gets the top 3 torrents as a JSON

    :torrent: (str) -> The name of the torrent whether it be a movie, game, book, etc.
    :return: (JSON) JSON of top 3 torrents
    '''

    return responses.JSONResponse(pirate_api.get_torrents(torrent))