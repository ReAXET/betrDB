"""Module to get NBA roster data from the nba_api package. These functions
will be used to populate the NBA roster table in the database. This will attempt
to get all roster data from 1996 to the current season."""

# Import statements
from typing import Any, List, Dict, Tuple, Union, Optional, Sequence
import os
import sys
import json
import time
import datetime
from datetime import date
from datetime import timedelta

import numpy as np
import pandas as pd
import requests
import psycopg2
from psycopg2 import sql


from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import playerdashboardbyyearoveryear
from nba_api.stats.endpoints import playerfantasyprofile
from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.endpoints import playerprofilev2

from betrdb.database import pg_sql 
from betrdb.common.logger import logger


# Logging
logger = logger
logger.info("Imported nba_roster.py")


# Get all NBA teams
def get_teams() -> list[Any]:
    """Get all NBA teams from the nba_api package."""
    logger.info("Getting all NBA teams.")
    nba_teams = teams.get_teams()
    return nba_teams


