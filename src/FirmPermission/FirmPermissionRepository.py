from src.FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from src.__Parents.Repository import Repository
from .FirmPermissionModel import FirmPermission
from src.Role.RoleModel import RoleFirmPermission


class FirmPermissionRepository(Repository, IFirmPermissionRepo):
    firm_permission: FirmPermission = FirmPermission
    role_firm_permission: RoleFirmPermission = RoleFirmPermission

    #                         PRODUCT

    def create(self, firm_permissions):
        firm_permission_list: list = []
        for firm_permission in firm_permissions:
            firm_permission_model = self.firm_permission()
            firm_permission_model.name = firm_permission['name']
            firm_permission_model.title = firm_permission['title']
            # firm_permission_model.client_id = client_id
            # firm_permission_model.firm_id = firm_id
            # firm_permission_model.roles.append(user.role)
            firm_permission_list.append(firm_permission_model)
        self.firm_permission.save_all_db(firm_permission_list)

    def get_by_id(self, firm_permission_id: int) -> FirmPermission:
        firm_permission = self.firm_permission.query.filter_by(id=firm_permission_id).first()
        return firm_permission

    def delete(self, firm_id: int):
        firm_permissions: list[FirmPermission] = self.firm_permission.query.filter_by(firm_id=firm_id).all()
        self.role_firm_permission.query.filter(self.role_firm_permission.firm_permission_id.in_(
            [firm_permission.id for firm_permission in firm_permissions]
        )).delete()

        for firm_permission in firm_permissions:
            firm_permission.delete_db()

    def delete_all_firm_permissions_by_role_id(self, role_id: int):
        self.role_firm_permission.query.filter_by(role_id=role_id).delete()

    def get_all(self) -> list[FirmPermission]:
        firm_permissions: list[FirmPermission] = FirmPermission.query.all()
        return firm_permissions

    def get_all_by_user_id(self, user_id: int):
        firm_permissions: list[FirmPermission] = FirmPermission.query.join(FirmPermission.roles).filter_by(user_id=user_id).all()
        return firm_permissions

