from src import db
from src.__Parents.Model import Model


class FirmProvision(db.Model, Model):
    title = db.Column(db.String(80))
    email_address = db.Column(db.String(80))
    activity_address = db.Column(db.String(80))
    legal_address = db.Column(db.String(80))
    phone_number = db.Column(db.BigInteger)

    hvhh = db.Column(db.String(120))
    chapter_registration_number = db.Column(db.BigInteger)
    tax_area_code = db.Column(db.BigInteger)
    insurer_account_number = db.Column(db.BigInteger)
    shiper_registration_book_number = db.Column(db.String(120))

    firm_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
