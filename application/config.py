from os import getenv

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", 'postgresql://USER:PASSWORD@localhost:5432/APPLICATION_DB')


class Config(object):  # default
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    # HOST = 'http://localhost'  #
    # PORT = '5000'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ENV = 'testing'
