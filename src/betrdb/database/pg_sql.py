"""Main connection to the PostgreSQL database."""

import sys
from pathlib import Path
from uuid import uuid4

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import (URL, create_engine)
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import Session, sessionmaker
from typing_extensions import Annotated

from betrdb.common.logger import logger
from betrdb.core.config import settings
from betrdb.models.base import MappedBase
from betrdb.utilities import uuid6
from betrdb.utilities.uuid6 import uuid6

# Load the .env file
env_path = Path(__file__).parents[3] / ".env"

load_dotenv(dotenv_path=env_path)


# Create a function to connect to the database
def create_engine_and_session(url: str | URL):
    """Create a connection to the database and return the engine and session."""
    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)
    return engine, session


def create_async_engine_and_session(url: str | URL):
    """Create a connection to the database and return the engine and session in async mode."""
    try:
        engine = create_async_engine(
            url, echo=settings.PG_ECHO, future=True, pool_pre_ping=True)
        logger.info("Engine created")
    except Exception as e:
        logger.error(f"Error creating engine: {e}")
        sys.exit(1)
    else:
        db_session = async_sessionmaker(
            bind=engine, expire_on_commit=False, autoflush=False)
        logger.info("Session created")
        return engine, db_session


# SQLAlchmey URL Sync
SQLALCHEMY_DATABASE_URL = settings.PG_URL
SQLALCHEMY_DATABASE_URL_ASYNC = settings.PG_URL_ASYNC

sync_engine, sync_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)
async_engine, async_db_session = create_async_engine_and_session(
    SQLALCHEMY_DATABASE_URL_ASYNC)


def get_sync_db_session():
    """Return a synchronous database session."""
    try:
        db = sync_session()
        yield db
    finally:
        db.close()  # type: ignore


async def get_async_db_session():
    """Return an asynchronous database session."""
    session = async_db_session()
    try:
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()


# Session Annotated
SyncSession = Annotated[Session, Depends(get_sync_db_session)]
CurrentAsyncSession = Annotated[AsyncSession, Depends(get_async_db_session)]


async def create_tables():
    """Create tables in the database."""
    async with async_engine.begin() as conn:
        await conn.run_sync(MappedBase.metadata.create_all)
        logger.info("Tables created")


def sync_create_tables():
    """Create tables in the database."""
    MappedBase.metadata.create_all(sync_engine)
    logger.info("Tables created")


def uuid4_str():
    """Return a UUID4 as a string."""
    return str(uuid4())


def uuid6_str():
    """Return a UUID6 as a string."""
    return str(uuid6())
