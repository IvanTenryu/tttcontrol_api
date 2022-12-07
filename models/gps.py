from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base
from .sim import Sim

Base = declarative_base()

class Gps (Base):
    __tablename__ = "gps"
    serial = Column (Integer, primary_key=True) 
    imei = Column (Integer)
    description = Column (String (100)) 
    software_version = Column (String (100))
    firmware_version = Column (String (100))
    status = Column (Integer) 
    comments = Column (String (255))
    sim_telephone = Column (Integer, ForeignKey (Sim.telephone))
    created_at = Column (TIMESTAMP)
    updated_at = Column (TIMESTAMP)
    deleted_at = Column (TIMESTAMP)
    created_by = Column (Integer)
    updated_by = Column (Integer)
    deleted_by = Column (Integer)

    def __repr__(self):
        return f"Gps(serial={self.serial!r}, sim_telephone={self.sim_telephone!r}, imei={self.imei!r}, description={self.description!r})"