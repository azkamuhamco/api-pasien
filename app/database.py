from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine   = create_engine("mysql+pymysql://root:@localhost:3306/zicare", pool_pre_ping=True, pool_recycle=300)
Session  = sessionmaker(bind=engine)
session  = scoped_session(Session)