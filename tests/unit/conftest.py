import pytest

import tempfile, os

from app import create_app, db

basedir = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def app():

    app = create_app()
    app.config.from_object("app.config.TestingConfig")

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    client = app.test_client()
    return client

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
