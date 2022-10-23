from src.__Parents.Controller import Controller
from .InvoiceService import InvoiceService
from .InvoiceRepository import InvoiceRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .InvoiceValidator import invoice_schema
from src.Unit.UnitRepository import UnitRepository
from src.Storage.StorageRepository import StorageRepository
from src.Colleague.ColleagueRepository import ColleagueRepository
from src.InvoiceNameList.InvoiceNameListRepository import InvoiceNameListRepository


class InvoiceController(Controller):

    invoice_service: InvoiceService = InvoiceService(InvoiceRepository(), UnitRepository(), StorageRepository(), ColleagueRepository(), InvoiceNameListRepository())

    @expects_json(invoice_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('invoice_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.invoice_service.create(body=self.request.get_json())
        return res

    @expects_json(invoice_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('invoice_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.invoice_service.update(invoice_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('invoice_edit')
    def delete(self) -> dict:
        res: dict = self.invoice_service.delete(self.id)
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('invoice_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.invoice_service.get_by_id(self.id)
        elif self.arguments.get('document_number') == 'true':
            res: dict = self.invoice_service.get_document_number()
        else:
            res: dict = self.invoice_service.get_all(page=self.page, per_page=self.per_page)
        return res


