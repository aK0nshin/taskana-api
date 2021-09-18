import logging

from pydantic import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool
    LOG_LEVEL: str
    API_V1_STR: str = '/api/v1'
    DB_URL: str

    @validator('LOG_LEVEL')
    def log_level_validator(cls, log_level): # noqa
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f'Invalid log level: {log_level}')
        return log_level

    class Config:
        env_file_encoding = 'utf-8'


settings = Settings()
