from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    # Relationship to ChatHistory
    chat_history = db.relationship('ChatHistory', back_populates='user', lazy=True)

class ChatHistory(db.Model):
    __tablename__ = 'chat_history'

    chat_id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    request_time = db.Column(db.DateTime, default=func.now())
    response_time = db.Column(db.DateTime, default=func.now())

    # Foreign Key to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    user = db.relationship('User', back_populates='chat_history')

class RecentChats(db.Model):
    __tablename__ = 'recent_chats'
    recent_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recent_time = db.Column(db.DateTime, default=func.now())

    # Relationship to User
    user = db.relationship('User', backref='recent_chats', lazy=True)
