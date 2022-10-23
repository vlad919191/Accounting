from abc import ABC, abstractmethod
from .InvoiceModel import Invoice


class IInvoiceRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> Invoice:
        pass

    @abstractmethod
    def update(self, invoice: Invoice, body: dict):
        pass

    @abstractmethod
    def delete(self, invoice: Invoice):
        pass

    @abstractmethod
    def get_by_id(self, invoice_id: int) -> Invoice:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int):
        pass

    @abstractmethod
    def get_by_document_number(self, document_number: str) -> Invoice:
        pass
    #
    # @abstractmethod
    # def create_invoice_name_lists(self, invoice_name_lists: list[dict], invoice_id: int):
    #     pass
    #
    # @abstractmethod
    # def update_invoice_name_lists(self, invoice_name_lists: list[dict], invoice_id: int):
    #     pass
