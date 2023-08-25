import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://m1016m:3SEOJjK0BODmVoultGEnkr4ggM7pLi16@dpg-cja6902683bs739mocc0-a.singapore-postgres.render.com/mspa'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
