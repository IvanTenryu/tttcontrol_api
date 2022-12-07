from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)
    name = Column (String (255))
    login = Column (String(255))
    password = Column (String(255))
    user_type = Column (Integer)
    status = Column (Integer)
    created_at = Column (TIMESTAMP)
    updated_at = Column (TIMESTAMP)
    deleted_at = Column (TIMESTAMP)
    created_by = Column (Integer)
    updated_by = Column (Integer)
    deleted_by = Column (Integer) 

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.status!r})"
