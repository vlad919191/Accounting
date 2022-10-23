from typing import List

from .IRoleRepo import IRoleRepo
from .RoleModel import Role, RolePermission, RoleFirmPermission
from flask import g
from ..__Parents.Repository import Repository


class RoleRepository(IRoleRepo, Repository):
    def create(self, body: dict, permissions: list, firm_permissions: list, client_id: int, creator_id: int or None,):
        role: Role = Role()
        role.name = body['name']
        role.description = body['description']
        role.permissions = permissions
        role.firm_permissions = firm_permissions
        role.client_id = client_id
        role.creator_id = creator_id
        role.save_db()

    def update(self, role: Role, body: dict, permissions: list, firm_permissions: list):
        role.name = body['name']
        role.description = body['description']
        role.permissions = permissions
        role.firm_permissions = firm_permissions
        role.update_db()

    def delete(self, role: Role):
        role.delete_db()

    def get_by_id(self, role_id: int) -> Role:
        role: Role = Role.query.filter_by(id=role_id, client_id=g.client_id).first()
        return role

    def get_first(self, client_id: int) -> Role:
        role: Role = Role.query.filter_by(client_id=client_id).first()
        return role

    def get_by_name(self, name: str):
        role: Role = Role.query.filter_by(name=name, client_id=g.client_id).first()
        return role

    def get_by_name_exclude_id(self, role_id: int, name: str) -> Role:
        role: Role = Role.query.filter_by(name=name, client_id=g.client_id).filter(Role.id != role_id).first()
        return role

    def get_all(self) -> List:
        roles: List[Role] = Role.query.filter_by(client_id=g.client_id, creator_id=g.user_id).all()
        for role in roles:
            role.users_count = len(role.users)
            del role.users

        return roles

    def get_all_by_ids(self, role_ids: list[int]):
        roles: List[Role] = Role.query.filter_by(client_id=g.client_id)\
            .filter(Role.creator_id.isnot(None), Role.id.in_(role_ids)).all()
        return roles
    #
    # def delete_role_permissions_by_role_id(self, role_id: int):
    #     RolePermission.query.filter_by(role_id=role_id).delete()
    #
    # def delete_all_role_firm_permissions_by_role_id(self, role_id: int):
    #     RoleFirmPermission.query.filter_by(role_id=role_id).delete()

    def cancel(self, role: Role):
        # role.users = []
        role.firm_permissions = []
        role.permissions = []
        role.update_db()