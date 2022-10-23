from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Service(Model, db.Model):
    code = db.Column(db.String(120))
    title = db.Column(db.String(120))

    check = db.Column(db.String(120))
    wholesale_price = db.Column(db.Numeric(10, 2))
    retail_price = db.Column(db.Numeric(10, 2))

    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))
    unit = relationship("Unit")

    firm_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
