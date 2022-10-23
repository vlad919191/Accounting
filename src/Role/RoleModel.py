from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


# class RoleFirmPermission(Model, db.Model):
#     role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
#     firm_permission_id = db.Column(db.Integer, db.ForeignKey("firm_permission.id"))


class RolePermission(Model, db.Model):
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"))


class RoleFirmPermission(Model, db.Model):
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    firm_permission_id = db.Column(db.Integer, db.ForeignKey("firm_permission.id"))


class Role(Model, db.Model):
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(120))
    client_id = db.Column(db.Integer)

    permissions = relationship("Permission", secondary="role_permission", backref=db.backref('role'))
    firm_permissions = relationship("FirmPermission", secondary="role_firm_permission", backref=db.backref('role'))
    users = relationship("User", secondary="user_role_firm", backref=db.backref('role'))

    creation_date = db.Column(db.DateTime, default=func.now())
    creator_id = db.Column(db.Integer)
