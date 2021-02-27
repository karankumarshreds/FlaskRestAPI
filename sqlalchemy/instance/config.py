import os

class Config(object):
    ''' Parent configuration base class '''
    DEBUG = False
    CSRF_ENABLED = True 
    SECRET = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True 

class TestingConfig(Config):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False