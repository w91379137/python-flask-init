
# 忽略警告
import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)

from flask import Flask
import pytest

from asabulu.util import create_app
from asabulu.service import main

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///../../tests/temp.db',
    })
    yield app
    print('\n○■ app close after test')

@pytest.fixture
def client(app: Flask):
    return app.test_client()

@pytest.fixture
def runner(app: Flask):
    return app.test_cli_runner()

@pytest.fixture
def db(app: Flask):
    with app.app_context():

        from asabulu.service import db
        main.db = db.init_app(app)
        
        yield main.db
        
        main.db.drop_all()
        main.db.session.commit()
        print('\n○■ db clear after test')

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
