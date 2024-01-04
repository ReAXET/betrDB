"""Custom Logger for BETR-DB"""
from __future__ import annotations   # allow self-reference in type hints

import os

from typing import TYPE_CHECKING

from loguru import logger

from betrdb.core.config import settings

from betrdb.core import paths_config

if TYPE_CHECKING:
    import loguru


class BetrLogger:

    def __init__(self):
        self.log_path = paths_config.LOG_PATH

    def log(self) -> loguru.Logger:
        """Custom logger for BETR-DB."""
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        log_stdout_file = os.path.join(self.log_path, settings.LOG_STDOUT_FILE)
        log_stderr_file = os.path.join(self.log_path, settings.LOG_STDERR_FILE)

        log_config = dict(rotation='10 MB', retention='10 days',
                          compression='zip', enqueue=True)

        logger.add(
            log_stdout_file,  # type: ignore
            level='INFO',
            filter=lambda record: record["level"].name == "INFO" or record["level"].no <= 25,
            **log_config,  # type: ignore
            backtrace=True,
            diagnose=True,
            colorize=True,


        )  # type: ignore
        return logger


logger = BetrLogger().log()
