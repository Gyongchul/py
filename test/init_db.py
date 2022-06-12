from curses import echo
from email.mime import base
from enum import auto
from statistics import covariance
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

userName = "fm_admin"
userPass = "longzhe@0206"
dbHost = "localhost"
dbPort = "3306"
dbName = "fm"

mysql_url = "mysql+pymysql://{userName}:{urlquote(password)}@{dbHost}:{dbPort}/dbName?charset=utf8"
engine = create_engine(mysql_url, echo = True )

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    Base.metadata.create_all(bind=engine)