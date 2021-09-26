from app.database.session import get_session


def get_db_session():
    try:
        db = get_session()
        yield db
    finally:
        db.close()