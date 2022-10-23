from .IInvoiceTypeRepo import IInvoiceTypeRepo
from .InvoiceTypeModel import InvoiceType


class InvoiceTypeRepository(IInvoiceTypeRepo):

    def create(self, body: dict):
        invoice_type: InvoiceType = InvoiceType()
        invoice_type.name = body['name']
        invoice_type.description = body['description']
        invoice_type.save_db()

    def update(self, invoice_type: InvoiceType, body: dict):
        invoice_type.name = body['name']
        invoice_type.description = body['description']
        invoice_type.update_db()

    def delete(self, invoice_type: InvoiceType):
        invoice_type.delete_db()

    def get_by_id(self, invoice_type_id: int) -> InvoiceType:
        invoice_type: InvoiceType = InvoiceType.query.filter_by(id=invoice_type_id).first()
        return invoice_type

    def get_all(self) -> list[InvoiceType]:
        invoice_types: list[InvoiceType] = InvoiceType.query.all()
        return invoice_types
    