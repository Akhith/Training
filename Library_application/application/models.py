"""Data models."""
# from application.__init__ import db
from . import db

class Book(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'Book'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    author = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    price = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )
    quantity = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )
    total = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=True
    )
    

    def __repr__(self):
        return '<Book {}>'.format(self.name)