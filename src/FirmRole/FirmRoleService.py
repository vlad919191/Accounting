# from .IFirmRoleRepo import IFirmRoleRepo
# from ..__Parents.Repository import Repository
# from ..__Parents.Service import Service
# from flask import g
#
#
# class FirmRoleService(Service, Repository):
#
#     def __init__(self, firm_role_repository: IFirmRoleRepo):
#         self.firm_role_repository: IFirmRoleRepo = firm_role_repository
#
#     # FIND PERMISSION FROM G.ROLE.FIRM_PERMISSION IN PERMISSION IDS
#     @staticmethod
#     def get_firm_permissions_by_firm_role_id(firm_permission_ids: list) -> list:
#         found_firm_permissions: list = []
#         for firm_permission_id in firm_permission_ids:
#             for g_firm_role in g.firm_roles:
#                 for g_firm_permission in g_firm_role.permissions:
#                     if firm_permission_id in g_firm_permission.id:
#                         found_firm_permissions.append(g_firm_permission)
#         return found_firm_permissions
#
#     def create(self, body: dict) -> dict:
#         if self.firm_role_repository.get_by_name(body['name']):
#             return self.response_conflict('firm role by this name exist')
#
#         self.firm_role_repository.create(
#             body=body,
#             firm_permissions=self.get_firm_permissions_by_firm_role_id(body['firm_permissions_ids']),
#             client_id=g.client_id)
#
#         return self.response_created('firm_role successfully created')
#
#     def update(self, firm_role_id: int, body: dict) -> dict:
#         firm_role = self.firm_role_repository.get_by_id(firm_role_id)
#         if not firm_role:
#             return self.response_not_found('firm_role not found')
#
#         if self.firm_role_repository.get_by_name_exclude_id(firm_role_id=firm_role_id, name=body['name']):
#             return self.response_conflict('firm role by this name exist')
#
#         self.firm_role_repository.update(firm_role, body, firm_permissions=[])
#         return self.response_updated('firm_role successfully updated')
#
#     def delete(self, firm_role_id: int) -> dict:
#         firm_role = self.firm_role_repository.get_by_id(firm_role_id)
#         if not firm_role:
#             return self.response_not_found('firm_role not found')
#
#         if len(firm_role.users):
#             return self.response_forbidden('данный объект нельзя удалить так как кнему ссылаются другие объекты ')
#         else:
#             self.firm_role_repository.cancel(firm_role)
#             self.firm_role_repository.delete(firm_role)
#
#         return self.response_deleted('firm_role successfully deleted')
#
#     def get_by_id(self, firm_role_id: int) -> dict:
#         firm_role = self.firm_role_repository.get_by_id(firm_role_id)
#         if not firm_role:
#             return self.response_not_found('firm_role not found')
#
#         return self.response_ok({
#             'id': firm_role.id,
#             'name': firm_role.name,
#             'description': firm_role.description,
#             'firm_permissions': self.get_array_items(firm_role.firm_permissions)
#         })
#
#     def get_all(self) -> dict:
#         firm_roles = self.firm_role_repository.get_all()
#         return self.response_ok(self.get_array_items(firm_roles))
