from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Firm(Model, db.Model):
    title = db.Column(db.String(40), nullable=False)
    email_address = db.Column(db.String(80), nullable=False)
    activity_address = db.Column(db.String(80), nullable=False)
    legal_address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)

    hvhh = db.Column(db.BigInteger)
    tax_area_code = db.Column(db.BigInteger)
    chapter_registration_number = db.Column(db.BigInteger)
    insurer_account_number = db.Column(db.BigInteger)

    sphere_id = db.Column(db.Integer, db.ForeignKey('sphere.id'))
    sphere = relationship("Sphere")

    client_id = db.Column(db.Integer)
