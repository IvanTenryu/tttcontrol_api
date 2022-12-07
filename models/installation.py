from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base
from .user import User

Base = declarative_base()

class Installation (Base):
    __tablename__ = "installation"
    id = Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey(User.id))
    date = Column (TIMESTAMP)
    vehicle_description = Column (String (50))
    economic_number = Column (String(20))
    plate = Column (String(20))
    gps_tag = Column (String(10))
    fuse_status = Column (String (10))
    installation_energy_type = Column (String(50))
    ignition_control = Column (Integer)
    ignition_detection = Column (Integer)
    odometer = Column (Integer)
    extra_control = Column (String(30))
    user_validator = Column (String(30))
    created_at = Column (TIMESTAMP)
    updated_at = Column (TIMESTAMP)
    deleted_at = Column (TIMESTAMP)
    created_by = Column (Integer)
    updated_by = Column (Integer)
    deleted_by = Column (Integer)

    def __repr__(self):
        return f"Installation(id={self.id!r}, user_id={self.user_id!r}, vehicle_description={self.vehicle_description!r})"