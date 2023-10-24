from application.util import generate

class Config(object):
    SECRET_KEY = generate(50)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'xclow3n'
    MYSQL_PASSWORD = 'xclow3n'
    MYSQL_DB = 'spellbound_servant'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True