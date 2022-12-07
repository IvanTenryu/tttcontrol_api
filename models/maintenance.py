from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base
from .user import User

Base = declarative_base()

class Maintenance (Base):
    __tablename__ = "maintenance"
    id = Column (Integer, primary_key=True)
    date = Column (TIMESTAMP)
    economic_number = Column (String(30))
    issue_description = Column (String (255))
    gps_tag = Column (String(10))
    fuse_status = Column (String(10))
    installation_energy_type = Column (String (50))
    installation_status = Column (String (255))
    switch = Column (String(4))
    new_tag = Column (String(10))
    user_validator = Column (String(30))
    user_id = Column (Integer, ForeignKey (User.id))
    created_at = Column (TIMESTAMP)
    updated_at = Column (TIMESTAMP)
    deleted_at = Column (TIMESTAMP)
    created_by = Column (Integer)
    updated_by = Column (Integer)
    deleted_by = Column (Integer)

    def __repr__(self):
        return f"Maintenance(id={self.id!r}, date={self.date!r}, issue_description={self.issue_description!r}, user_id={self.user_id!r})"
