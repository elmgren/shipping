import logging
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass


def _get_url():
    try:
        return os.getenv("DBSTRING")
    except KeyError as exception:
        logger.error(f"Environment variable not set {exception}")
        sys.exit(1)


def get_session():
    engine = create_engine(_get_url())
    session_class = sessionmaker(bind=engine)
    return session_class()
