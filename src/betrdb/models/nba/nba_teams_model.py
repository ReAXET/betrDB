"""Models for NBA teams."""
from datetime import datetime

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from betrdb.database.pg_sql import uuid4_str
from betrdb.models.base import Base, id_key
from betrdb.utilities.timezone import timezone

####################################################################################################
# NBA Team Model
####################################################################################################


class NbaTeam(Base):

    __tablename__ = 'nba_teams'  # type: ignore

    id: Mapped[id_key] = mapped_column(init=False)
    uuid: Mapped[str] = mapped_column(
        String, init=False, default_factory=uuid4_str, unique=True)
    team_id: Mapped[int] = mapped_column(String, nullable=False, unique=True)
    abbreviation: Mapped[str] = mapped_column(String, nullable=True)
    city: Mapped[str] = mapped_column(String, nullable=True)
    conference: Mapped[str] = mapped_column(String, nullable=True)
    division: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    nickname: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    state: Mapped[str] = mapped_column(String, nullable=True)
    year_founded: Mapped[int] = mapped_column(String, nullable=True)
    is_all_star_team: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Relationships
    # players: Mapped[Optional[list[NbaPlayer]]] = relationship('NbaPlayer', back_populates='team')
    # games: Mapped[Optional[list[NbaGame]]] = relationship('NbaGame', back_populates='team')

    created_at: Mapped[datetime] = mapped_column(
        String, nullable=False, default=timezone.now)
    updated_at: Mapped[datetime] = mapped_column(
        String, nullable=False, default=timezone.now, onupdate=timezone.now)

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"<NbaTeam(id={self.id}, uuid={self.uuid}, team_id={self.team_id}, abbreviation={self.abbreviation}, city={self.city}, conference={self.conference}, division={self.division}, full_name={self.full_name}, name={self.name}, state={self.state}, year_founded={self.year_founded}, is_all_star_team={self.is_all_star_team}, created_at={self.created_at}, updated_at={self.updated_at})>"
