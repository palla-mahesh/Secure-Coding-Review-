from app import DB
from flask_login import UserMixin

class User(DB.Model, UserMixin):

    id = DB.Column(DB.Integer, primary_key=True)

    username = DB.Column(
        DB.String(100),
        unique=True,
        nullable=False
    )

    email = DB.Column(
        DB.String(100),
        unique=True,
        nullable=False
    )

    password = DB.Column(
        DB.String(300),
        nullable=False
    )