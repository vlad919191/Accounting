from src.__Parents.Controller import Controller
from .InvoiceTypeService import InvoiceTypeService
from .InvoiceTypeRepository import InvoiceTypeRepository


class InvoiceTypeController(Controller):
    invoice_type_service: InvoiceTypeService = InvoiceTypeService(InvoiceTypeRepository())

    def get(self) -> dict:
        res: dict = self.invoice_type_service.get_all()
        return res
