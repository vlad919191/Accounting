from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Colleague(Model, db.Model):
    title = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(80), nullable=False)

    hvhh = db.Column(db.BigInteger)

    addresses = relationship("Address")
    client_id = db.Column(db.Integer)
