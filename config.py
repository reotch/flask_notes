class Config(object):
    DEBUG=False
    TESTING=False
    DATABASE_URI='sqlite://:memory:'

class ProductionConfig(Config):
    SECRET_KEY='f7abf44bc5f2e87ffef64fa220aaed518aad4761c4e56fc613'


class DevelopmentConfig(Config):
    ENV='development'
    SECRET_KEY='1cedef555f2877263c878e2c5f8f0fec2b1ab3c23b4b622252'
    DEBUG=True

class TestingConfig(Config):
    TESTING=True