class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configs
    """
    
    SQLALCHEMY_ECHO = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    """
    Production configs
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Tesing Configurations
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing' : TestingConfig
}
