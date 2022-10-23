from src import db
from src.__Parents.Model import Model


class InvoiceType(db.Model, Model):
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
