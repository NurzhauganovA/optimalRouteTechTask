from distutils.util import strtobool

import environ
import pathlib

from pydantic_settings import BaseSettings


BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env('DEBUG', cast=strtobool, default=False)

    POSTGRES_USER: str = env('POSTGRES_USER', default='postgres')
    POSTGRES_PASSWORD: str = env('POSTGRES_PASSWORD', default='postgres')
    POSTGRES_SERVER: str = env('POSTGRES_SERVER', default='localhost')
    POSTGRES_PORT: str = env('POSTGRES_PORT', default='5432')
    POSTGRES_DB: str = env('POSTGRES_DB', default='postgres')
    SQLALCHEMY_DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
