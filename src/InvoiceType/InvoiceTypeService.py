from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IInvoiceTypeRepo import IInvoiceTypeRepo


class InvoiceTypeService(Service, Repository):

    def __init__(self, invoice_type_repository: IInvoiceTypeRepo):
        self.invoice_type_repository: IInvoiceTypeRepo = invoice_type_repository

    def get_all(self) -> dict:
        invoice_types = self.invoice_type_repository.get_all()
        return self.response_ok(self.get_array_items(invoice_types))
