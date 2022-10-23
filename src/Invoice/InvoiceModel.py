from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Invoice(db.Model, Model):
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

    date = db.Column(db.Date())
    document_number = db.Column(db.String(80))
    buyer_account = db.Column(db.String(80))

    bar_code = db.Column(db.String(180))
    contract = db.Column(db.String(80))
    contact_date = db.Column(db.Date())
    prepaid_account = db.Column(db.String(80))

    aah_account = db.Column(db.String(80))
    out_type = db.Column(db.String(80))

    series_and_number = db.Column(db.String(120))
    out_date = db.Column(db.Date())
    provider_id = db.Column(db.Integer, db.ForeignKey("firm.id"))
    provider = relationship("Firm")

    buyer_id = db.Column(db.Integer, db.ForeignKey('colleague.id'))
    buyer = relationship("Colleague")
    invoice_name_lists = relationship("InvoiceNameList")

    firm_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)

