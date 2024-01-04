"""Database utilities for the BETR-DB package. This module contains functions
that are used to interact with the database. This includes functions to create
the database, create tables, and insert data into the tables. This module also
contains functions to get the column names from the tables in the database. """
# Import statements
from betrdb.data.nba_utils import chunk_list, progress_bar
from betrdb.common.logger import logger
from betrdb.data.constants import DB_NAME, SEASON_ID



def insert_many(settings, table, rows):
    """Inserts a list of rows into a table in the database."""
    logger.info(f"Inserting {len(rows)} rows into {table.name} table.")
    chunked_rows = chunk_list(rows, settings.batch_size)
    with settings.db.atomic():
        for chunk in chunked_rows:
            table.insert_many(chunk).execute()
    logger.info(f"Inserted {len(rows)} rows into {table.name} table.")
    return True


def insert_many_on_conflict_ignore(settings, table, rows):
    """Inserts a list of rows into a table in the database. If there is a
    conflict, ignore the row."""
    logger.info(f"Inserting {len(rows)} rows into {table.name} table.")
    with settings.db.atomic():
        table.insert_many(rows).on_conflict_ignore().execute()
    logger.info(f"Inserted {len(rows)} rows into {table.name} table.")
    return True

