# from src.__Parents.Controller import Controller
# from .FirmRoleService import FirmRoleService
# from .FirmRoleRepository import FirmRoleRepository
# from src.Auth.AuthMiddleware import AuthMiddleware
# from src.Permission.PermissionMiddleware import PermissionMiddleware
#
#
# class FirmRoleController(Controller):
#     firm_role_service: FirmRoleService = FirmRoleService(FirmRoleRepository())
#
#     @AuthMiddleware.check_authorize
#     @PermissionMiddleware.check_permission('firm_role_edit')
#     def post(self) -> dict:
#         res: dict = self.firm_role_service.create(self.request.get_json())
#         return res
#
#     @AuthMiddleware.check_authorize
#     @PermissionMiddleware.check_permission('firm_role_edit')
#     def put(self) -> dict:
#         res: dict = self.firm_role_service.update(self.id, self.request.get_json())
#         return res
#
#     @AuthMiddleware.check_authorize
#     @PermissionMiddleware.check_permission('firm_role_edit')
#     def delete(self) -> dict:
#         res: dict = self.firm_role_service.delete(self.id)
#         return res
#
#     @AuthMiddleware.check_authorize
#     @PermissionMiddleware.check_permission('firm_role_get')
#     def get(self) -> dict:
#         if self.id:
#             res: dict = self.firm_role_service.get_by_id(self.id)
#         else:
#             res: dict = self.firm_role_service.get_all()
#         return res
