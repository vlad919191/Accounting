from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


# class RoleFirmPermission(Model, db.Model):
#     role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
#     firm_permission_id = db.Column(db.Integer, db.ForeignKey("firm_permission.id"))
#
#
# class UserRoleFirm(Model, db.Model):
#     firm_id = db.Column(db.Integer, db.ForeignKey("firm.id"))
#     role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#
# class FirmRole(Model, db.Model):
#     name = db.Column(db.String(60), nullable=False)
#     description = db.Column(db.String(120))
#     client_id = db.Column(db.Integer)
#
#     firm_permissions = relationship("FirmPermission", secondary="role_firm_permission", backref=db.backref('firm_role'))
#     users = relationship("User")
#
#     creation_date = db.Column(db.DateTime, default=func.now())
