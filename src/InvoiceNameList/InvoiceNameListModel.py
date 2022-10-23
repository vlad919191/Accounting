from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class InvoiceNameList(db.Model, Model):
    invoice_type_id = db.Column(db.Integer, db.ForeignKey("invoice_type.id"))
    invoice_type = relationship("InvoiceType")
    
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    storage = relationship("Storage")

    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"))
    unit = relationship("Unit")

    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    invoice = relationship("Invoice")

    count = db.Column(db.Numeric(8, 2))
    price = db.Column(db.Numeric(8, 2))

    aah = db.Column(db.Boolean)
    expense_account = db.Column(db.String(180))
    income_account = db.Column(db.String(180))

    batch = db.Column(db.String(80))
    creation_date = db.Column(db.Date(), default=datetime.utcnow())

    firm_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
