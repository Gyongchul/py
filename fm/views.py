from re import L
from fm import app
from fm.models import Laser
from fm.init_db import db_session
from sqlalchemy.exc import SQLAlchemyError



@app.route('/')
def idx():
   try:
      lsr = Laser("part_id","part_name","youben","NTC", 1, 2)
      db_session.add(lsr)
      db_session.commit()
      print("sussess insert ===================================================")
   except SQLAlchemyError as sqlerror:
      db_session.rollback()
      print("sqlError==============================================================", sqlerror)
   except:
      print("Eror")


   return "susses!!"