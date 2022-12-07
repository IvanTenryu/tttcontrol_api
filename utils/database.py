from curses import echo
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config.config import db_module, db_user, db_pass, db_host, db_port, db_name

def get_db_session ():
    database_url = f"mysql+{db_module}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    print (database_url)
    engine = create_engine (database_url)
    session = Session (engine)
    return session
