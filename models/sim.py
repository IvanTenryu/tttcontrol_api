from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Sim (Base):
    __tablename__ = "sim"
    telephone = Column (Integer, primary_key=True)
    account = Column (String (15))
    father_account = Column (String (15))
    iccid = Column (String(25))
    package = Column (String(20))
    status = Column (Integer)
    cancellation_date = Column (TIMESTAMP)
    created_at = Column (TIMESTAMP)
    updated_at = Column (TIMESTAMP)
    deleted_at = Column (TIMESTAMP)
    created_by = Column (Integer)
    updated_by = Column (Integer)
    deleted_by = Column (Integer)

    def __repr__(self):
        return f"Sim(telephone={self.telephone!r}, account={self.account!r}, iccid={self.iccid!r})"
