from src.FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from src.Permission.IPermissionRepo import IPermissionRepo
from src.Role.IRoleRepo import IRoleRepo
from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from flask import g


class RoleService(Service, Repository):
    def __init__(self, role_repository: IRoleRepo):
        self.role_repository: IRoleRepo = role_repository

    # FIND PERMISSION FROM G.USER.PERMISSION IN PERMISSION IDS
    @staticmethod
    def get_permissions_by_role_id(permission_ids: list) -> list:
        found_permissions: list = []

        for permission in g.permissions:
            if permission.id in permission_ids:
                found_permissions.append(permission)
        return found_permissions

    # FIRM PERMISSIONS FOUND FROM G FIRM ROLE
    @staticmethod
    def get_firm_permissions_by_firm_role_id(firm_permission_ids: list) -> list:
        found_firm_permissions: list = []
        for firm_permission_id in firm_permission_ids:
            for g_firm_permission in g.firm_permissions:
                if g_firm_permission.id == firm_permission_id:
                    found_firm_permissions.append(g_firm_permission)
        return found_firm_permissions

    def create(self, body: dict) -> dict:
        if self.role_repository.get_by_name(body['name']):
            return self.response_conflict('роль по данной названии уже существует')

        self.role_repository.create(
            body=body,
            permissions=self.get_permissions_by_role_id(permission_ids=body['permission_ids']),
            firm_permissions=self.get_firm_permissions_by_firm_role_id(body['firm_permission_ids']),
            client_id=g.client_id,
            creator_id=g.user.id
        )
        return self.response_created('роль успешно создана')

    def update(self, role_id: int, body: dict) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('роль не нейден')

        if self.role_repository.get_by_name_exclude_id(role_id, body['name']):
            return self.response_conflict('роль по данной названии уже существует')

        self.role_repository.update(
            role=role,
            body=body,
            permissions=self.get_permissions_by_role_id(permission_ids=body['permission_ids']),
            firm_permissions=self.get_firm_permissions_by_firm_role_id(firm_permission_ids=body['firm_permission_ids']),
        )
        return self.response_updated('роль успешно обновлена')

    def delete(self, role_id: int) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('роль не нейден')

        # self.role_repository.delete_all_role_firm_permissions_by_role_id(role_id=role_id)
        # self.role_repository.delete_role_permissions_by_role_id(role_id=role_id)
        if len(role.users):
            return self.response_forbidden('данный объект нельзя удалить так как кнему ссылаются другие объекты ')
        else:
            self.role_repository.cancel(role)
            self.role_repository.delete(role)

        return self.response_deleted('роль успешно удалена')

    def get_by_id(self, role_id: int) -> dict:
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return self.response_not_found('роль не нейден')

        return self.response_ok({
            'name': role.name,
            'description': role.description,
            'permissions': self.get_array_items(role.permissions),
            'firm_permissions': self.get_array_items(role.firm_permissions),
            'users_count': len(role.users)
        })

    def get_all(self) -> dict:
        roles = self.role_repository.get_all()
        for role in roles:
            del role.permissions
            del role.firm_permissions

        return self.response_ok(self.get_array_items(roles))
