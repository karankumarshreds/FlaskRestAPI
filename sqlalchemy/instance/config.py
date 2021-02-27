import os


## Config class contains the general settings that we want 
## all environments to have by default. Other environment 
## classes inherit from it and can be used to set settings 
## that are only unique to them.

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


app_config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'stage': StagingConfig,
    'prod': ProductionConfig
}