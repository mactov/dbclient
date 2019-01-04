import sys
import os
import json
from urllib.request import urlopen


SERVER_URL = 'http://localhost:5000/'
ROOT_PATH = '/Users/mactov/projects/dbclient/'

def setup():
    if os.path.isfile(ROOT_PATH + 'servers.ini'):
        if os.path.isfile(ROOT_PATH + 'test_servers.ini'):
            os.rename(ROOT_PATH + 'servers.ini', ROOT_PATH + 'servers.ini.old')
            os.rename(ROOT_PATH + 'test_servers.ini', ROOT_PATH + 'servers.ini')

def teardown():
    if os.path.isfile(ROOT_PATH + 'servers.ini'):
        if os.path.isfile(ROOT_PATH + 'servers.ini.old'):
            os.rename(ROOT_PATH + 'servers.ini', ROOT_PATH + 'test_servers.ini')
            os.rename(ROOT_PATH + 'servers.ini.old', ROOT_PATH + 'servers.ini')

def test_get_servers():
    url = SERVER_URL + 'servers'
    response = urlopen(url).read()
    assert response.decode("utf-8").replace('\n', '').replace(' ','') == \
           json.dumps([{"server": "localhost"}, {"server": "db.ultech.fr"}]).replace(' ','')

def test_get_one_server():
    url = SERVER_URL + 'server/localhost'
    response = urlopen(url).read()
    assert response.decode("utf-8").replace('\n', '').replace(' ','') == \
           json.dumps({"server": "localhost","engine": "postgresql",
                       "host": "localhost","port": "5432","user": "postgres",
                       "password": "pass"}).replace(' ','')    

