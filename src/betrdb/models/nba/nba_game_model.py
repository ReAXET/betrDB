"""Models for NBA games."""
from typing import Any

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from betrdb.models.base import Base, id_key


class NBAGame(Base):
    """Model for NBA games."""
    __tablename__ = 'nba_games'  # type: ignore

    # Columns
    id = id_key()
    game_id = Column(String, nullable=False, unique=True)
    season_id = Column(String, nullable=False)
    game_date = Column(DateTime, nullable=False)
    home_team_id = Column(Integer, ForeignKey('nba_teams.id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('nba_teams.id'), nullable=False)
    home_team_score = Column(Integer, nullable=False)
    away_team_score = Column(Integer, nullable=False)
    home_team_win = Column(Boolean, nullable=False)
    home_team_cover = Column(Boolean, nullable=False)
    home_team_cover_spread = Column(Integer, nullable=False)
    home_team_cover_spread_result = Column(String, nullable=False)
    total_game_points_combined = Column(Integer, nullable=False)
    total_game_points_over = Column(Boolean, nullable=False)
    total_game_points_over_result = Column(String, nullable=False)
    total_game_points_under = Column(Boolean, nullable=False)
    total_game_points_under_result = Column(String, nullable=False)
    home_team_money_line = Column(Integer, nullable=False)
    away_team_money_line = Column(Integer, nullable=False)
    home_team_money_line_win = Column(Boolean, nullable=False)
    home_team_money_line_win_result = Column(String, nullable=False)
    away_team_money_line_win = Column(Boolean, nullable=False)
    away_team_money_line_win_result = Column(String, nullable=False)

    # Relationships
    home_team: Any = relationship('NBATeam', foreign_keys=[
                                  home_team_id], backref=backref('home_games', lazy='dynamic'))
    away_team: Any = relationship('NBATeam', foreign_keys=[
                                  away_team_id], backref=backref('away_games', lazy='dynamic'))

    def __repr__(self) -> str:
        """String representation of the NBAGame model."""
        return f"<NBAGame(game_id='{self.game_id}', season_id='{self.season_id}', game_date='{self.game_date}', home_team_id='{self.home_team_id}', away_team_id='{self.away_team_id}', home_team_score='{self.home_team_score}', away_team_score='{self.away_team_score}', home_team_win='{self.home_team_win}', home_team_cover='{self.home_team_cover}', home_team_cover_spread='{self.home_team_cover_spread}', home_team_cover_spread_result='{self.home_team_cover_spread_result}', total_game_points_combined='{self.total_game_points_combined}', total_game_points_over='{self.total_game_points_over}', total_game_points_over_result='{self.total_game_points_over_result}', total_game_points_under='{self.total_game_points_under}', total_game_points_under_result='{self.total_game_points_under_result}', home_team_money_line='{self.home_team_money_line}', away_team_money_line='{self.away_team_money_line}', home_team_money_line_win='{self.home_team_money_line_win}', home_team_money_line_win_result='{self.home_team_money_line_win_result}', away_team_money_line_win='{self.away_team_money_line_win}', away_team_money_line_win_result='{self.away_team_money_line_win_result}')>"


class NBAGameStats(Base):
    """Model for NBA game stats."""
    __tablename__ = 'nba_game_stats'  # type: ignore

    # Columns
    id = id_key()
    game_id = Column(String, nullable=False)
    season_id = Column(String, nullable=False)
    game_date = Column(DateTime, nullable=False)
    team_id = Column(Integer, ForeignKey('nba_teams.id'), nullable=False)
    team_score = Column(Integer, nullable=False)
    team_win = Column(Boolean, nullable=False)
    team_cover = Column(Boolean, nullable=False)
    team_cover_spread = Column(Integer, nullable=False)
    team_cover_spread_result = Column(String, nullable=False)
    total_game_points_combined = Column(Integer, nullable=False)
    total_game_points_over = Column(Boolean, nullable=False)
    total_game_points_over_result = Column(String, nullable=False)
    total_game_points_under = Column(Boolean, nullable=False)
    total_game_points_under_result = Column(String, nullable=False)
    team_money_line = Column(Integer, nullable=False)
    team_money_line_win = Column(Boolean, nullable=False)
    team_money_line_win_result = Column(String, nullable=False)

    # Relationships
    team: Any = relationship('NBATeam', foreign_keys=[
                             team_id], backref=backref('game_stats', lazy='dynamic'))

    def __repr__(self) -> str:
        """String representation of the NBAGameStats model."""
        return f"<NBAGameStats(game_id='{self.game_id}', season_id='{self.season_id}', game_date='{self.game_date}', team_id='{self.team_id}', team_score='{self.team_score}', team_win='{self.team_win}', team_cover='{self.team_cover}', team_cover_spread='{self.team_cover_spread}', team_cover_spread_result='{self.team_cover_spread_result}', total_game_points_combined='{self.total_game_points_combined}', total_game_points_over='{self.total_game_points_over}', total_game_points_over_result='{self.total_game_points_over_result}', total_game_points_under='{self.total_game_points_under}', total_game_points_under_result='{self.total_game_points_under_result}', team_money_line='{self.team_money_line}', team_money_line_win='{self.team_money_line_win}', team_money_line_win_result='{self.team_money_line_win_result}')>"
