from datetime import date, datetime
import email
from email.policy import default
from enum import unique
from tokenize import String
from pymysql import Date
from sqlalchemy import VARCHAR, Column, Integer, DATETIME, column
from fm.init_db import Base



class Laser(Base):
    __tablename__ = 'laser'

# Member variable is Cloum
    id = Column(Integer, primary_key = True)
    pid = Column(Integer, default = 1)
    part_id = Column(VARCHAR)
    part_name = Column(VARCHAR)
    part_worker = Column(VARCHAR)
    part_deviceNo = Column(VARCHAR)
    part_qty = Column(Integer)
    laser_qty = Column(Integer)
    create_date = Column(DATETIME, default = datetime.utcnow)
    update_date = Column(DATETIME, default = datetime.utcnow)

    def __init__(self, part_id=None, part_name=None, part_worker=None, part_deviceNo=None, part_qty=0, laser_qty=1):
    
        self.part_id = part_id
        self.part_name = part_name
        self.part_worker = part_worker
        self.part_deviceNo = part_deviceNo
        self.part_qty = part_qty
        self.laser_qty = laser_qty


    def __repr__(self):
        return 'Laser %r, %r, %r, %r, %r, %r' % (self.part_id, self.part_name, self.part_worker, self.part_deviceNo, self.part_qty, self.laser_qty)