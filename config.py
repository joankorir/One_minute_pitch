import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'kyle'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joan:ray@localhost/pitchminute'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch Minute'
    SENDER_EMAIL = 'joankorir44@gmail.com'

    @staticmethod
    def init_app(app):
       pass

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joan:ray@localhost/pitchminute_test'
    pass


class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joan:ray@localhost/pitchminute'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
