# from flask import g
#
# from src.FirmRole.IFirmRoleRepo import IFirmRoleRepo
# from .FirmRoleModel import FirmRole
#
#
# class FirmRoleRepository(IFirmRoleRepo):
#
#     def create(self, body: dict, firm_permissions: list, client_id: int):
#         firm_role: FirmRole = FirmRole()
#         firm_role.name = body['name']
#         firm_role.description = body['description']
#         firm_role.firm_permissions = firm_permissions
#         firm_role.client_id = client_id
#         firm_role.save_db()
#
#     def update(self, firm_role: FirmRole, body: dict, firm_permissions: list):
#         firm_role.name = body['name']
#         firm_role.description = body['description']
#         firm_role.firm_permissions = firm_permissions
#         firm_role.save_db()
#
#     def delete(self, firm_role: FirmRole):
#         firm_role.delete_db()
#
#     def get_by_id(self, firm_role_id: int) -> FirmRole:
#         firm_role: FirmRole = FirmRole.query.filter_by(id=firm_role_id, client_id=g.client_id)
#         return firm_role
#
#     def get_first(self, client_id) -> FirmRole:
#         firm_role: FirmRole = FirmRole.query.filter_by(client_id=client_id).first()
#         return firm_role
#
#     def get_all_by_ids(self, firm_role_ids: list[int]) -> list[FirmRole]:
#         roles: list[FirmRole] = FirmRole.query.filter_by(client_id=g.client_id).filter(FirmRole.id.in_(firm_role_ids)).all()
#         return roles
#
#     def get_by_name_exclude_id(self, firm_role_id: int, name: str) -> FirmRole:
#         firm_role: FirmRole = FirmRole.query.filter_by(name=name).filter(FirmRole.id != firm_role_id).first()
#         return firm_role
#
#     def get_all(self) -> list:
#         firm_roles: list[FirmRole] = FirmRole.query.filter_by(client_id=g.client_id).all()
#         for firm_role in firm_roles:
#             firm_role.users_count = len(firm_role.users)
#             del firm_role.users
#
#         return firm_roles
#
#     def get_by_name(self, name: str) -> FirmRole:
#         firm_role: FirmRole = FirmRole.query.filter_by(name=name).first()
#         return firm_role
#
#     def cancel(self, firm_role: FirmRole):
#         firm_role.users = []
#         firm_role.firm_permissions = []
#         firm_role.update_db()
