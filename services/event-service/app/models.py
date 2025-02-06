from .utils import db
from datetime import datetime

class Event(db.Model):
    __tablename__="events"

    # Primary
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(200),
        unique=False,
        nullable=False
    )

    description = db.Column(
        db.String(500),
        unique=False,
        nullable=False
    )

    location = db.Column(
        db.String(200),
        unique=False,
        nullable=True
    )

    is_virtual = db.Column(
        db.Boolean,
        default=False,
        nullable=True
    )

    date = db.Column(
        db.Date
    )

    time = db.Column(
        db.Time
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
        return '<Event %r>' %(self.name)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'is_virtual': self.is_virtual,
            'date': self.date,
            'time': str(self.time)
        }
