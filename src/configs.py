"""App Configuration"""
# pylint: disable=too-few-public-methods
from decouple import config


class AppConfig():
    """Base configuration"""
    HOST = config('HOST', default='0.0.0.0')
    PORT = config('PORT', default=9000, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)
