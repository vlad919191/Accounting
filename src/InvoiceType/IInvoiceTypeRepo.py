from abc import ABC, abstractmethod
from .InvoiceTypeModel import InvoiceType


class IInvoiceTypeRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, invoice_type: InvoiceType, body: dict):
        pass

    @abstractmethod
    def delete(self, invoice_type: InvoiceType):
        pass

    @abstractmethod
    def get_by_id(self, invoice_type_id: int) -> InvoiceType:
        pass

    @abstractmethod
    def get_all(self) -> list[InvoiceType]:
        pass
