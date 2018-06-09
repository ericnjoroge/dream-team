class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configs
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    """
    Production configs
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
