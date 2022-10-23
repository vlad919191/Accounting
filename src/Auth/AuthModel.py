from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Auth(Model, db.Model):
    user_id = db.Column(db.Integer, nullable=False)
    access_token = db.Column(db.String(320), nullable=False)
    user_role_firm_id = db.Column(db.Integer, db.ForeignKey('user_role_firm.id'))
    user_role_firm = relationship("UserRoleFirm")
    # refresh_token = db.Column(db.String(320), nullable=False)

    def __init__(self, user_id: int):
        self.user_id = user_id
