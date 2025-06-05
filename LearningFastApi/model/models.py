﻿from sqlalchemy import Column, Integer, DateTime, String, func, TIMESTAMP, text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from LearningFastApi.db.database import base

class Post(base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean,server_default='TRUE' ,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete='CASCADE'), nullable=False)
    
    owner = relationship("User")

class User(base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=False)
    
class Vote(base):
    __tablename__ = 'votes'
    user_id = Column(Integer,ForeignKey("users.id", ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id", ondelete='CASCADE'), primary_key=True)
    
    
