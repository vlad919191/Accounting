from src.__Parents.Controller import Controller
from .FirmProvisionService import FirmProvisionService
from .FirmProvisionRepository import FirmProvisionRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .FirmProvisionValidator import firm_provision_schema


class FirmProvisionController(Controller):
    firm_provision_service: FirmProvisionService = FirmProvisionService(FirmProvisionRepository())

    @expects_json(firm_provision_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('firm_provision_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.firm_provision_service.create(self.request.get_json())
        return res

    @expects_json(firm_provision_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('firm_provision_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.firm_provision_service.update(self.id, self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('firm_provision_edit')
    def delete(self) -> dict:
        res: dict = self.firm_provision_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('firm_provision_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.firm_provision_service.get_by_id(self.id)
        else:
            res: dict = self.firm_provision_service.get_all(self.page, self.per_page)
        return res

