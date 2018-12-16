import json
from urllib.request import urlopen

from behave import *

SERVER_URL = 'http://localhost:5000/'

@given('The localhost and db.iablaka.com are in the server list')
def step_impl(context):
    pass

@when('I list them')
def step_impl(context):
    url = SERVER_URL + 'servers'
    context.response = urlopen(url).read()


@then('I get this [{"server": "localhost"}, {"server": "db.iablaka.com"}]')
def step_impl(context):
    assert context.response.decode("utf-8") == json.dumps([{"server": "localhost"}, {"server": "db.iablaka.com"}])