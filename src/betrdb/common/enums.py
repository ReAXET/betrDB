"""Enums for the betrdb package."""

from enum import Enum
from enum import IntEnum as SourceIntEnum
from typing import Type


class _EnumBase:
    """Base class for all enums in the package."""

    @classmethod
    def get_member_keys(cls: Type[Enum]) -> list[str]:  # type: ignore
        """Get the keys of all members of the enum."""
        return [name for name, _ in cls.__members__.keys()]

    @classmethod
    def get_member_values(cls: Type[Enum]) -> list:  # type: ignore
        """Get the values of all members of the enum."""
        return [item.value for item in cls.__members__.values()]


class IntEnum(SourceIntEnum, _EnumBase):
    """Base class for all IntEnums in the package."""
    pass


class StrEnum(str, Enum, _EnumBase):
    """Base class for all StrEnums in the package."""
    pass


class MenuType(IntEnum):
    """Enum for the different types of menus."""
    directory = 0
    menu = 1
    button = 2
    separator = 3
    submenu = 4


class RoleDataScopeType(IntEnum):
    """Enum for the different types of role data scopes."""
    all = 0
    custom = 1


class MethodType(StrEnum):
    """Enum for the different types of methods."""
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class LoginLogStatusType(IntEnum):
    """Enum for the different types of login log statuses."""
    failure = 0
    success = 1


class BuildTreeType(StrEnum):
    """Enum for the different types of build trees."""
    traversal = 'traversal'
    recursive = 'recursive'


class StatusType(IntEnum):
    """Enum for the different types of statuses."""
    disabled = 0
    enabled = 1
