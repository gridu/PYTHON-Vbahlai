import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer


if (os.path.exists(str(os.getcwd()) + '\database.db')):
    os.remove(str(os.getcwd()) + '\database.db')

engine = create_engine('sqlite:///' + str(os.getcwd()) + '\database.db', echo=True)
Base = declarative_base()

class Author(Base):
    __tablename__= 'authors'
    url = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)
    job_title = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    articles_counter = Column(Integer, nullable=True)
    counter = 0

class Article(Base):
    __tablename__ = 'articles'
    url = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    publication_date = Column(String, nullable=False)
    author_url = Column(String, nullable=False)
    tags = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()