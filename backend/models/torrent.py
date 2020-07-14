from pydantic import BaseModel

class Torrent(BaseModel):
    name: str
    magnet: str
    size: str
    category: str