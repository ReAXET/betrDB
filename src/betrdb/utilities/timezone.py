"""Custom Timezone Utilities"""

import pytz
import zoneinfo
from datetime import datetime, timedelta

from betrdb.core.config import settings


class Timezone:
    """Timezone Utilities"""

    def __init__(self, tz: str = settings.DATETIME_TIMEZONE):
        self.tz_info = pytz.timezone(tz) or zoneinfo.ZoneInfo(tz)

    def now(self) -> datetime:
        """Return the current time in the timezone."""
        return datetime.now(self.tz_info)

    def f_datetime(self, dt: datetime) -> datetime:
        """Return the datetime in the timezone."""
        return dt.astimezone(self.tz_info)

    def f_str(self, date_str: str, format_str: str = settings.DATETIME_FORMAT) -> datetime:
        """Return the datetime string in the timezone."""
        return datetime.strptime(date_str, format_str).replace(tzinfo=self.tz_info)


timezone = Timezone()
