#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:01:00 2023

Configuration file for BETR-DB
    
"""
from __future__ import annotations   # allow self-reference in type hints
from functools import lru_cache
from typing import Literal
import os


from dotenv import load_dotenv
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')

    # Database connection
    PG_HOST: str = os.getenv('PG_HOST', 'localhost')
    PG_PORT: int = os.getenv('PG_PORT', 5432)  # type: ignore
    PG_USER: str = os.getenv('PG_USER', 'postgres')
    PG_PASSWORD: str = os.getenv('PG_PASSWORD', 'postgres')
    PG_DATABASE: str = os.getenv('PG_DATABASE', 'postgres')
    PG_CONNECTION_STRING: str = os.getenv('PG_CONNECTION_STRING', '')
    PG_URL: str = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'  # noqa: E501
    PG_URL: str = PG_CONNECTION_STRING if PG_CONNECTION_STRING else PG_URL
    PG_ECHO: bool = True if os.getenv('PG_ECHO', False) else False
    PG_URL_ASYNC: str = os.getenv('PG_URL_ASYNC', '')  # noqa: E501

    # Redis
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT: int = os.getenv('REDIS_PORT', 6379)  # type: ignore
    REDIS_PASSWORD: str = os.getenv('REDIS_PASSWORD', '')
    REDIS_DB: int = os.getenv('REDIS_DB', 0)  # type: ignore

    # Logging
    LOG_LEVEL: Literal['DEBUG', 'INFO',
                       'WARNING', 'ERROR', 'CRITICAL'] = 'INFO'
    LOG_STDOUT_FILE: str = 'betrdb_access.log'
    LOG_STDERR_FILE: str = 'betrdb_error.log'
    LOG_FILE_MAX_BYTES: int = 1024 * 1024 * 10  # 10 MB

    # API
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'BetrDB API'
    DESCRIPTION: str = 'API for the BETR-DB'
    VERSION: str = '0.1.0'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOC_URL: str | None = f'{API_V1_STR}/redoc'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi.json'

    # Uvicorn
    UVICORN_HOST: str = os.getenv('UVICORN_HOST', 'localhost')
    UVICORN_PORT: int = os.getenv('UVICORN_PORT', 8000)  # type: ignore
    UVICORN_RELOAD: bool = os.getenv('UVICORN_RELOAD', False)  # type: ignore

    # DateTimes Formats
    DATETIME_TIMEZONE: str = 'America/New_York'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    # Caching
    CACHE_EXPIRE: int = 3600  # 1 hour
    CACHE_KEY_PREFIX: str = 'fastapi_cache'
    CACHE_KEY: str = '{prefix}:{key}'
    CACHE_BACKEND: str = 'redis'
    CACHE_REDIS_URL: str = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    CACHE_REDIS_PASSWORD: str | None = REDIS_PASSWORD
    CACHE_REDIS_DB: int = REDIS_DB
    CACHE_REDIS_ENCODING: str = 'utf-8'

    # Token
    TOKEN_SECRET_KEY: str = os.getenv('TOKEN_SECRET_KEY', '')
    TOKEN_ALGORITHM: str = 'HS256'
    TOKEN_EXPIRE_MINUTES: int = 30
    TOKEN_URL_SWAGGER: str = f'{API_V1_STR}/auth/swagger_login'
    TOKEN_REDIS_PREFIX: str = 'betrdb_token'
    TOKEN_REDIS_URL: str = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
