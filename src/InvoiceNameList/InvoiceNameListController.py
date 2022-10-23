from src.__Parents.Controller import Controller
from .InvoiceNameListService import InvoiceNameListService
from .InvoiceNameListRepository import InvoiceNameListRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .InvoiceNameListValidator import invoice_name_list_schema
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from datetime import datetime


class InvoiceNameListController(Controller):
    invoice_name_list_service: InvoiceNameListService = InvoiceNameListService(InvoiceNameListRepository())

    # @expects_json(invoice_name_list_schema)
    # @AuthMiddleware.check_authorize
    # def post(self) -> dict:
    #     res: dict = self.invoice_name_list_service.create(self.request.get_json())
    #     return res

    @expects_json(invoice_name_list_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.invoice_name_list_service.update(self.id, self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.invoice_name_list_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('invoice_statistic_get')
    def get(self) -> dict:
        res: dict = self.invoice_name_list_service.get_all_by_date(
            start_date=datetime.strptime(self.arguments.get('start_date'), '%Y-%m-%d'),
            end_date=datetime.strptime(self.arguments.get('end_date'), '%Y-%m-%d'))
        return res
    #
    # @AuthMiddleware.check_authorize
    # def get(self) -> dict:
    #     if self.id:
    #         res: dict = self.invoice_name_list_service.get_by_id(self.id)
    #     else:
    #         res: dict = self.invoice_name_list_service.get_all(self.arguments.get('invoice_id'))
    #     return res
