# All variables should be uppercase

class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://tissues:fuckherhard@localhost/testing'
    SQLALCHEMY_ECHO = True
    SECRET_KEY = "sldjfhals13 2hhdwflkjdhfa"