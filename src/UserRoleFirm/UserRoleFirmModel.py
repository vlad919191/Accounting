from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class UserRoleFirm(Model, db.Model):
    firm_id = db.Column(db.Integer, db.ForeignKey("firm.id"))
    firm = relationship("Firm")

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = relationship("Role")
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

