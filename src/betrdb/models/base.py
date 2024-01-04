"""Core SQLAlchemy models for the BETR-DB application."""

from datetime import datetime

from sqlalchemy.orm import (DeclarativeBase, Mapped, MappedAsDataclass,
                            declared_attr, mapped_column)
from typing_extensions import Annotated

from betrdb.utilities.timezone import timezone

id_key = Annotated[
    int, mapped_column(primary_key=True, index=True,
                       autoincrement=True, sort_order=-999, comment="Primary key")

]


class UserMixin(MappedAsDataclass):
    """Mixin class for user-related fields."""

    create_user: Mapped[int] = mapped_column(
        sort_order=998, comment="User ID of the creator of the record")
    update_user: Mapped[int | None] = mapped_column(
        init=False, default=None, sort_order=998, comment="User ID of the last updater of the record")


class DateTimeMixin(MappedAsDataclass):
    """Mixin class for datetime-related fields."""

    create_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=timezone.now, sort_order=999, comment="Time of the creation of the record"
    )
    update_time: Mapped[datetime | None] = mapped_column(
        init=False, onupdate=timezone.now, sort_order=999, comment="Time of the last update of the record"
    )


class MappedBase(DeclarativeBase):
    """Base class for all mapped classes."""

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Automatically set the table name to the class name."""
        return cls.__name__.lower()


class DataclassBase(MappedAsDataclass, MappedBase):
    """Base class for all dataclass mapped classes."""

    __abstract__ = True


class Base(DataclassBase, DateTimeMixin):
    """Base class for all mapped classes."""

    __abstract__ = True
