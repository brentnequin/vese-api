import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', "").replace("postgres://", "postgresql://", 1) or 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):

    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'