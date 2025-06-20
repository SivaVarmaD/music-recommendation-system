from sqlalchemy import create_engine, Column, Integer, String, Date, Table, MetaData
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.exc import NoResultFound

DATABASE_URL = 'sqlite:///mydatabase.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    author = Column(String, nullable=False)
    language = Column(String, nullable=False)
    genre = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    friends = Column(String, nullable=False)  # Storing JSON as TEXT
    likedmusic = Column(String, nullable=False)  # Storing JSON as TEXT

Base.metadata.create_all(bind=engine)
