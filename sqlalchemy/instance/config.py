import os

class Config(object):
    ''' Parent configuration class '''
    DEBUG = False
    CSRF_ENABLED = True 
    SECRET = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')