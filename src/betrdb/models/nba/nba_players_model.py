from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from betrdb.database.pg_sql import uuid4_str
from betrdb.models.base import Base, id_key
from betrdb.utilities.timezone import timezone

####################################################################################################
# NBA Player Model
####################################################################################################


class NbaPlayer(Base):

    __tablename__ = 'nba_players'  # type: ignore

    id: Mapped[id_key] = mapped_column(init=False)
    uuid: Mapped[str] = mapped_column(
        String, init=False, default_factory=uuid4_str, unique=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    player_id: Mapped[int] = mapped_column(String, nullable=False, unique=True)
    college_name: Mapped[str] = mapped_column(String, nullable=True)
    country: Mapped[str] = mapped_column(String, nullable=True)
    draft_year: Mapped[int] = mapped_column(String, nullable=True)
    draft_round: Mapped[int] = mapped_column(String, nullable=True)
    draft_number: Mapped[int] = mapped_column(String, nullable=True)
    height: Mapped[float] = mapped_column(String, nullable=True)
    weight: Mapped[float] = mapped_column(String, nullable=True)
    season_exp: Mapped[int] = mapped_column(String, nullable=True)

    # Relationships
    # team: Mapped[Optional[NbaTeam]] = relationship('NbaTeam', back_populates='players')
    # team_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('nba_teams.id'), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        String, nullable=False, default=timezone.now)
    updated_at: Mapped[datetime] = mapped_column(
        String, nullable=False, default=timezone.now, onupdate=timezone.now)

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"<NbaPlayer(id={self.id}, uuid={self.uuid}, first_name={self.first_name}, last_name={self.last_name}, full_name={self.full_name}, player_id={self.player_id}, college_name={self.college_name}, country={self.country}, draft_year={self.draft_year}, draft_round={self.draft_round}, draft_number={self.draft_number}, height={self.height}, weight={self.weight}, season_exp={self.season_exp}, created_at={self.created_at}, updated_at={self.updated_at})>"


####################################################################################################
