from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship


class AuthRestore(db.Model, Model):
    ticket = db.Column(db.String(180), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
