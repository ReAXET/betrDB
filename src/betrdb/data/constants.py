"""All data constants for the betrdb."""

# Import statements
from datetime import datetime
from typing import Any, Optional, Union, Iterable


# Constants
SEASON_ID = 'season_id'
SEASON = 'season'
SEASON_TYPE = 'season_type'
TEAM_ID = 'team_id'
TEAM_ABBREVIATION = 'team_abbrv'
TEAM_CITY = 'team_city'
TEAM_NAME = 'team_name'
TEAM_NICKNAME = 'team_nickname'
TEAM_YEAR_FOUNDED = 'team_year_founded'
TEAM_CONFERENCE = 'team_conference'
TEAM_DIVISION = 'team_division'
TEAM_CODE = 'team_code'
GAME_ID = 'game_id'
GAME_DATE = 'game_date'
GAME_TIME = 'game_time'

# Database constants
DB_NAME = 'betrdb'

# Table names
NBA_GAME = 'nba_game'
NBA_GAME_STATS = 'nba_game_stats'
NBA_GAME_STATS_ADVANCED = 'nba_game_stats_advanced'
NBA_GAME_STATS_MISC = 'nba_game_stats_misc'
NBA_GAME_STATS_SCORING = 'nba_game_stats_scoring'
NBA_GAME_STATS_USAGE = 'nba_game_stats_usage'
NBA_GAME_STATS_TRACKING = 'nba_game_stats_tracking'
NBA_GAME_STATS_FANTASY = 'nba_game_stats_fantasy'
NBA_GAME_STATS_TEAM = 'nba_game_stats_team'
NBA_GAME_STATS_TEAM_ADVANCED = 'nba_game_stats_team_advanced'
NBA_GAME_STATS_TEAM_MISC = 'nba_game_stats_team_misc'
NBA_GAME_STATS_TEAM_SCORING = 'nba_game_stats_team_scoring'
NBA_GAME_STATS_TEAM_USAGE = 'nba_game_stats_team_usage'
NBA_GAME_STATS_TEAM_TRACKING = 'nba_game_stats_team_tracking'
NBA_GAME_STATS_TEAM_FANTASY = 'nba_game_stats_team_fantasy'
NBA_GAME_STATS_PLAYER = 'nba_game_stats_player'
NBA_GAME_STATS_PLAYER_ADVANCED = 'nba_game_stats_player_advanced'
NBA_GAME_STATS_PLAYER_MISC = 'nba_game_stats_player_misc'
NBA_GAME_STATS_PLAYER_SCORING = 'nba_game_stats_player_scoring'
NBA_GAME_STATS_PLAYER_USAGE = 'nba_game_stats_player_usage'
NBA_GAME_STATS_PLAYER_TRACKING = 'nba_game_stats_player_tracking'
NBA_GAME_STATS_PLAYER_FANTASY = 'nba_game_stats_player_fantasy'

# Headers dict
nba_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

nhl_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nhl-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-nhl-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nhl.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

nfl_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nfl-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-nfl-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nfl.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

mlb_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-mlb-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-mlb-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.mlb.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

ncaaf_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-ncaaf-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-ncaaf-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.ncaa.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

ncaab_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-ncaab-stats-token': 'true',
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ),
    'x-ncaab-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.ncaa.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}

# Team IDs
NBA_TEAM_ABBRV_MAP = {
    'ATL': 1610612737,
    'BOS': 1610612738,
    'BKN': 1610612751,
    'CHA': 1610612766,
    'CHI': 1610612741,
    'CLE': 1610612739,
    'DAL': 1610612742,
    'DEN': 1610612743,
    'DET': 1610612765,
    'GSW': 1610612744,
    'HOU': 1610612745,
    'IND': 1610612754,
    'LAC': 1610612746,
    'LAL': 1610612747,
    'MEM': 1610612763,
    'MIA': 1610612748,
    'MIL': 1610612749,
    'MIN': 1610612750,
    'NOP': 1610612740,
    'NYK': 1610612752,
    'OKC': 1610612760,
    'ORL': 1610612753,
    'PHI': 1610612755,
    'PHX': 1610612756,
    'POR': 1610612757,
    'SAC': 1610612758,
    'SAS': 1610612759,
    'TOR': 1610612761,
    'UTA': 1610612762,
    'WAS': 1610612764,
}

NBA_TEAM_ID_LIST = [
    1610612737,
    1610612738,
    1610612751,
    1610612766,
    1610612741,
    1610612739,
    1610612742,
    1610612743,
    1610612765,
    1610612744,
    1610612745,
    1610612754,
    1610612746,
    1610612747,
    1610612763,
    1610612748,
    1610612749,
    1610612750,
    1610612740,
    1610612752,
    1610612760,
    1610612753,
    1610612755,
    1610612756,
    1610612757,
    1610612758,
    1610612759,
    1610612761,
    1610612762,
    1610612764,
]

# NBA play by play EventMsgTypes
NBA_EVENTMSGTYPE_MAP = [
    {'id': 1, 'string': 'FIELD_GOAL_MADE'},
    {'id': 2, 'string': 'FIELD_GOAL_MISSED'},
    {'id': 3, 'string': 'FREE_THROW'},
    {'id': 4, 'string': 'REBOUND'},
    {'id': 5, 'string': 'TURNOVER'},
    {'id': 6, 'string': 'FOUL'},
    {'id': 7, 'string': 'VIOLATION'},
    {'id': 8, 'string': 'SUBSTITUTION'},
    {'id': 9, 'string': 'TIMEOUT'},
    {'id': 10, 'string': 'JUMP_BALL'},
    {'id': 11, 'string': 'EJECTION'},
    {'id': 12, 'string': 'PERIOD_BEGIN'},
    {'id': 13, 'string': 'PERIOD_END'},
    {'id': 14, 'string': 'UNKNOWN'},
    {'id': 15, 'string': 'STOPPAGE'},
    {'id': 16, 'string': 'START_OF_PERIOD'},
    {'id': 17, 'string': 'END_OF_PERIOD'},
    {'id': 18, 'string': 'GAME_BEGIN'},
    {'id': 19, 'string': 'GAME_END'},
    {'id': 20, 'string': 'REPLAY'},
    {'id': 21, 'string': 'JUMP_BALL_START'},
    {'id': 22, 'string': 'PERIOD_READY'},
    {'id': 23, 'string': 'SCORE'},
    {'id': 24, 'string': 'ENTER_GAME'},
    {'id': 25, 'string': 'PLAYER_VIOLATION'},
    {'id': 26, 'string': 'TEAM_VIOLATION'},
    {'id': 27, 'string': 'TIMEOUT_30SEC'},
    {'id': 28, 'string': 'TURNOVER_NO_ASSIST'},
    {'id': 29, 'string': 'TURNOVER_BAD_PASS'},
    {'id': 30, 'string': 'TURNOVER_LOST_BALL'},
    {'id': 31, 'string': 'TURNOVER_TRAVELING'},
    {'id': 32, 'string': 'TURNOVER_PALMING'},
    {'id': 33, 'string': 'TURNOVER_DOUBLE_DRIBBLE'},
    {'id': 34, 'string': 'TURNOVER_OUT_OF_BOUNDS'},
    {'id': 35, 'string': 'TURNOVER_OFFENSIVE'},
    {'id': 36, 'string': 'TURNOVER_SHOT_CLOCK'},
    {'id': 37, 'string': 'TURNOVER_OTHER'},
    {'id': 38, 'string': 'FOUL_PERSONAL'},
    {'id': 39, 'string': 'FOUL_SHOOTING'},
    {'id': 40, 'string': 'FOUL_LOOSE_BALL'},
    {'id': 41, 'string': 'FOUL_OFFENSIVE'},
    {'id': 42, 'string': 'FOUL_INBOUND'},
    {'id': 43, 'string': 'FOUL_TECHNICAL'},
    {'id': 44, 'string': 'FOUL_FLAGRANT1'},
    {'id': 45, 'string': 'FOUL_FLAGRANT2'},
    {'id': 46, 'string': 'FOUL_DOUBLE_TECHNICAL'},
    {'id': 47, 'string': 'FOUL_DEFENSIVE3SEC'},
    {'id': 48, 'string': 'FOUL_DELAY'},
    {'id': 49, 'string': 'FOUL_TAUNTING'},
    {'id': 50, 'string': 'FOUL_CHARGING'},
    {'id': 51, 'string': 'FOUL_BLOCKING'},
    {'id': 52, 'string': 'FOUL_OFF_BALL'},
    {'id': 53, 'string': 'FOUL_PLAYER_CONTROL'},
    {'id': 54, 'string': 'FOUL_SCREEN'},
    {'id': 55, 'string': 'FOUL_LOOSE_BALL_TECHNICAL'},
    {'id': 56, 'string': 'FOUL_OFFENSIVE_CHARGE'},
    {'id': 57, 'string': 'FOUL_OFFENSIVE_BLOCK'},
    {'id': 58, 'string': 'FOUL_SHOOTING_BLOCK'},
    {'id': 59, 'string': 'FOUL_FLAGRANT'},

]
