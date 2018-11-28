from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # one to many
    books = relationship('book')

class Book(Basse):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # foreign key
    user_id = Column(String(20), ForeignKey('user.id'))

# Finally when we query a User instance, the attribute books
# will return a list of instances of class Book.
