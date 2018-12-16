import sys 
import json
from urllib.request import urlopen

# sys.path.append('../')
# from api import *

SERVER_URL = 'http://localhost:5000/'

def test_get_servers():
    url = SERVER_URL + 'servers'
    response = urlopen(url).read()
    assert response.decode("utf-8") == json.dumps([{"server": "localhost"}, {"server": "db.ultech.fr"}])