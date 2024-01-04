"""Module for paths configuration."""

import os
from pathlib import Path

from betrdb.core.config import settings

ROOT_DIR = Path(__file__).resolve().parents[3]

BASE_PATH = Path(__file__).resolve().parents[2]

VERSIONS = os.path.join(BASE_PATH, 'src', 'alembic', 'versions')

LOG_PATH = os.path.join(BASE_PATH, 'src', 'betrdb', 'logs')

RAW_DATA_PATH = os.path.join(BASE_PATH, 'src', 'betrdb', 'data', 'raw')

PROCESSED_DATA_PATH = os.path.join(BASE_PATH, 'src', 'betrdb', 'data', 'processed')  # noqa: E501

MODELS_PATH = os.path.join(BASE_PATH, 'src', 'betrdb', 'models')

SCHEMAS_PATH = os.path.join(BASE_PATH, 'src', 'betrdb', 'schemas')
