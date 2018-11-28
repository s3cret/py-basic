from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base Class
Base = declarative_base()

class User(Base):
    # the table name
    __tablename__ = 'user'

    # the structure of the table
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# init database connection
# 'database_type+connector_name://username:password@hostname:port/database_name'
engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/database_name")
# create database session class bind with engine
# engine specify the info of the database you get to operate
DBSession = sessionmaker(bind=engine)
# create instance of session
session = DBSession()

new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()
# here you go, you insert into your database with one record

q_session = DBSession()
user = q_session.query(User).filter(User.id==5).one()
print(type(user))
print('name', user.name)
session.close()







