
# pytest -s tests/server/root/test_sayhello.py

from flask.app import Flask
from flask.testing import FlaskClient

def test_sayhello(app: Flask, client: FlaskClient):    
    
    response = client.get('/sayhello')
    data = response.get_data()
    # print(data)
    assert b'hello' in data

    response = client.post('/sayhello')
    data = response.get_data()
    # print(data)
    assert b'hello' in data