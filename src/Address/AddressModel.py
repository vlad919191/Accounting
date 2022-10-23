from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Address(Model, db.Model):
    activity_address = db.Column(db.String(80), nullable=False)
    legal_address = db.Column(db.String(80), nullable=False)

    phone_number = db.Column(db.Integer, nullable=False)
    account_number = db.Column(db.String(80))

    colleague_id = db.Column(db.Integer, db.ForeignKey("colleague.id"))
    colleague = relationship("Colleague")

    client_id = db.Column(db.Integer)
