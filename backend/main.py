from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import NoResultFound
from typing import List, Generator
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import date

DATABASE_URL = 'sqlite:///mydatabase.db'

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy models
class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    author = Column(String, nullable=False)
    language = Column(String, nullable=False)
    genre = Column(String, nullable=False)

class MusicCreateModel(BaseModel):
    name: str
    date: date
    author: str
    language: str
    genre: str

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    friends = Column(String, nullable=False)  # Storing JSON as TEXT
    likedmusic = Column(String, nullable=False)  # Storing JSON as TEXT

class UserCreateModel(BaseModel):
    friends: List[int]
    likedmusic: List[int]

Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get a SQLAlchemy session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MusicModel(BaseModel):
    id: int
    name: str
    date: date
    author: str
    language: str
    genre: str

    class Config:
        orm_mode = True

class UserModel(BaseModel):
    id: int
    friends: List[int]
    likedmusic: List[int]

    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"message": "Welcome to the Music API"}

@app.get("/music", response_model=List[MusicModel])
def get_music(db: Session = Depends(get_db)):
    music = db.query(Music).all()
    return music

@app.post("/music", response_model=MusicModel)
def add_music(music: MusicCreateModel, db: Session = Depends(get_db)):
    db_music = Music(
        name=music.name,
        date=music.date,
        author=music.author,
        language=music.language,
        genre=music.genre
    )
    db.add(db_music)
    db.commit()
    db.refresh(db_music)
    return db_music

@app.get("/users", response_model=List[UserModel])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [UserModel(id=user.id, friends=json.loads(user.friends), likedmusic=json.loads(user.likedmusic)) for user in users]

@app.post("/users", response_model=UserModel)
def add_user(user: UserModel, db: Session = Depends(get_db)):
    db_user = User(id=user.id, friends=json.dumps(user.friends), likedmusic=json.dumps(user.likedmusic))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

@app.post("/users/{user_id}/friends/{friend_id}")
def add_friend(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if user:
        friends = json.loads(user.friends)
        friends.append(friend_id)
        user.friends = json.dumps(friends)
        db.commit()
        return {"message": "Friend added successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/{user_id}/likedmusic/{music_id}")
def add_liked_music(user_id: int, music_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if user:
        likedmusic = json.loads(user.likedmusic)
        likedmusic.append(music_id)
        user.likedmusic = json.dumps(likedmusic)
        db.commit()
        return {"message": "Music added to liked list"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/users/{user_id}/friends", response_model=List[int])
def get_friends(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if user:
        return json.loads(user.friends)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/users/{user1_id}/suggest_song/{user2_id}", response_model=List[MusicModel])
def suggest_song(user1_id: int, user2_id: int, criteria: str, value: str, db: Session = Depends(get_db)):
    valid_criteria = ['author', 'language', 'genre']
    if criteria not in valid_criteria:
        raise HTTPException(status_code=400, detail="Invalid criteria. Must be one of 'author', 'language', or 'genre'.")

    user1 = db.query(User).filter(User.id == user1_id).one_or_none()
    user2 = db.query(User).filter(User.id == user2_id).one_or_none()

    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="One or both users have no liked music")

    user1_likedmusic = json.loads(user1.likedmusic)
    user2_likedmusic = json.loads(user2.likedmusic)

    if not user1_likedmusic or not user2_likedmusic:
        raise HTTPException(status_code=404, detail="One or both users have no liked music")

    user1_music = db.query(Music).filter(Music.id.in_(user1_likedmusic)).all()
    user2_music = db.query(Music).filter(Music.id.in_(user2_likedmusic)).all()

    if criteria == 'author':
        user1_filtered = [m for m in user1_music if m.author == value]
        user2_filtered = [m for m in user2_music if m.author == value]
    elif criteria == 'language':
        user1_filtered = [m for m in user1_music if m.language == value]
        user2_filtered = [m for m in user2_music if m.language == value]
    elif criteria == 'genre':
        user1_filtered = [m for m in user1_music if m.genre == value]
        user2_filtered = [m for m in user2_music if m.genre == value]

    common_music = [m for m in user1_filtered if m in user2_filtered]

    if not common_music:
        return {"message": "No common liked song found between the users"}

    suggested_songs = [MusicModel(id=m.id, name=m.name, date=m.date, author=m.author, language=m.language, genre=m.genre) for m in common_music]
    return suggested_songs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
