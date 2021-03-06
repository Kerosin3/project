from os import getenv, environ

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", 'postgresql://USER:PASSWORD@localhost:5432/APPLICATION_DB')


class Config(object):  # default
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_BINDS = {
        'test_db': 'postgresql://USER:TEST@localhost:5430/APPLICATION_DB_TEST',
    }
    SOME_OTHER_VAR = 'Some value'
    JOBS = [
        {
            "id": "job1",
            "func": "app:job1",
            "args": (),
            "trigger": "interval",
            "seconds": 5,
        },
        {
            "id": "job2",
            "func": "app:job_pseupo_update",
            "args": (),
            "trigger": "interval",
            "seconds": 5,
        },
        {
            "id": "job3",
            "func": "app:job_get_update_all_indexes",
            "args": (),
            "trigger": "interval",
            "seconds": 5,
        }
    ]
    SCHEDULER_API_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SOME_VALUE = 'AHAHAHA'
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'postgresql://USER:TEST@localhost:5430/APPLICATION_DB_TEST'
