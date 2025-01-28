from .utils import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    # Primary key
    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True
    )

    username = db.Column(
        db.String(80),
        unique=False,
        nullable=False
    )

    email = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String,
        unique=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    def __repr__(self):
        return '<User %r>' %(self.username)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
