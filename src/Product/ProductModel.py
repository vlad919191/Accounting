from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Product(Model, db.Model):
    name = db.Column(db.String(120))
    code = db.Column(db.String(120))
    description = db.Column(db.String(120))
    wholesale_price = db.Column(db.Numeric(10, 2))
    retail_price = db.Column(db.Numeric(10, 2))
    count = db.Column(db.Numeric(15, 1))

    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    product_type = relationship("ProductType")

    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))
    unit = relationship("Unit")

    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    storage = relationship("Storage")

    self_price = db.Column(db.Numeric(10, 2))

    client_id = db.Column(db.Integer)
    