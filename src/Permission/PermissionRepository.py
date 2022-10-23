from .IPermissionRepo import IPermissionRepo
from src.__Parents.Repository import Repository
from .PermissionModel import Permission
from ..User.UserModel import User
from src.Role.RoleModel import RolePermission


class PermissionRepository(Repository, IPermissionRepo):
    permission: Permission = Permission
    role_permission: RolePermission = RolePermission

    # CREATE
    def create(self, name: str, title: str) -> Permission:
        permission = self.permission()
        permission.name = name
        permission.title = title
        permission.save_db()
        return permission

    # GET BY ID
    def get_by_id(self, permission_id: int) -> Permission:
        permission = self.permission.query.filter_by(id=permission_id).first()
        return permission

    # GET ALL
    def get_all(self) -> list[dict]:
        permissions = self.permission.query.all()
        return permissions

    # GET BY NAME
    def get_by_name(self, name: str) -> Permission:
        permission = self.permission.query.filter_by(name=name).first()
        return permission

    # GET BY NAME USER ID
    def get_by_name_user_id(self, name: str, user_id: int) -> Permission:
        permission = self.permission.query.filter_by(name=name).join(Permission.users).filter(User.id == user_id).first()
        return permission

    # # DELETE USER PERMISSION
    # def delete_roler_permissions_by_user_id(self, role_id: int):
    #     self.role_permission.query.filter_by(role_id=role_id).delete()
    #
    # # GET BY ALL BY PARENT USER
    # def get_all_by_parent_user(self, user_id: int):
    #     permissions = self.permission.join(self.permission.users.any([]))


