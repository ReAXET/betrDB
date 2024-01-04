"""Module to retrieve NBA data from the nba_api package as well as data from the github repo of nba data, which 
was done to prevent the need to make API calls to the nba_api package."""

from pathlib import Path
from itertools import product
import urllib.request
import tarfile
from typing import List, Tuple, Dict, Union, Optional, Sequence
import pandas as pd
import numpy as np
from nba_api.stats.static import teams as nba_teams
from nba_api.stats.static import players as nba_players
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2, boxscoreadvancedv2, boxscoresummaryv2
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.library.parameters import SeasonTypeAllStar
from nba_api.stats.library.parameters import SeasonTypePlayoffs

from betrdb.common.logger import logger
from betrdb.core.config import settings
from betrdb.core.paths_config import RAW_DATA_PATH, PROCESSED_DATA_PATH


# Setup a Path object for the data directory
RAW_DATA_PATH = Path(RAW_DATA_PATH)
PROCESSED_DATA_PATH = Path(PROCESSED_DATA_PATH)


def get_nba_data(seasons: Union[Sequence, int] = range(1996, 2023),
                 data: Union[Sequence, str] = (
                     "datanba", "nbastats", "pbpstats", "shotdetail"),
                 seasontype: str = 'rg',
                 untar: bool = False,
                 ) -> None:
    """Loading nba play-by-play data from github repo https://github.com/shufinskiy/nba_data.

    Args:
        seasons(Union[Sequence, int]): Seasons to load data for. Defaults to range(1996, 2023).
        data(Union[Sequence, str]): Data to load. Defaults to ("datanba", "nbastats", "pbpstats", "shotdetail").
        seasontype(str): Season type to load. Defaults to 'rg'.
        untar(bool): Whether to untar the data. Defaults to False.

    Returns:
        None
    """
    if isinstance(seasons, int):
        seasons = (seasons,)
    if isinstance(data, str):
        data = (data,)

    if seasontype == 'rg':
        need_data = tuple(["_".join([data, str(season)])
                          for data, season in product(data, seasons)])
    elif seasontype == 'po':
        need_data = tuple(["_".join([data, seasontype, str(season)]) for (
            data, seasontype, season) in product(data, (seasontype,), seasons)])
    else:
        need_data_rg = tuple(["_".join([data, str(season)])
                             for data, season in product(data, seasons)])
        need_data_po = tuple(["_".join([data, seasontype, str(season)]) for (
            data, seasontype, season) in product(data, ('po',), seasons)])
        need_data = need_data_rg + need_data_po
    with urllib.request.urlopen("https://raw.githubusercontent.com/shufinskiy/nba_data/main/list_data.txt") as f:
        list_data = f.read().decode('utf-8').strip()

    name_v = [string.split("=")[0] for string in list_data.split("\n")]
    element_v = [string.split("=")[1] for string in list_data.split("\n")]

    need_name = [name for name in name_v if name in need_data]
    need_element = [element for (name, element) in zip(
        name_v, element_v) if name in need_data]

    for i in range(len(need_name)):
        t = urllib.request.urlopen(need_element[i])
        with open("".join([need_name[i], ".tar.xz"]), 'wb') as f:
            f.write(t.read())
        if untar:
            with tarfile.open("".join([need_name[i], ".tar.xz"])) as f:
                f.extract("".join([need_name[i], ".csv"]), './')

            Path("".join([need_name[i], ".tar.xz"])).unlink()


# Run the get_nba_data function to load the data
get_nba_data(seasons=range(1996, 2023), data=(
    "datanba", "nbastats", "pbpstats", "shotdetail"), seasontype='rg', untar=True)
