from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base
from .gps import Gps

Base = declarative_base()

class ChangeLog (Base):
    __tablename__ = "change_log"
    id = Column (Integer, primary_key=True)
    gps_serial = Column (Integer, ForeignKey(Gps.serial))
    date = Column (TIMESTAMP)
    type = Column (String(20))
    previous_value = Column (String (20))
    new_value = Column (String (20))

    def __repr__(self):
        return f"ChangeLog(id={self.id!r}, gps_serial={self.gps_serial!r}, new_value={self.new_value!r})"