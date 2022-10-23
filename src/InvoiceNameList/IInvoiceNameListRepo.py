from .InvoiceNameListModel import InvoiceNameList
from abc import ABC, abstractmethod
from datetime import datetime, date


class IInvoiceNameListRepo(ABC):
    @abstractmethod
    def create(self, body: dict, invoice_id: int):
        pass

    @abstractmethod
    def update(self, invoice_name_list: InvoiceNameList, body: dict):
        pass

    @abstractmethod
    def delete(self, invoice_name_list: InvoiceNameList):
        pass

    @abstractmethod
    def delete_all(self, invoice_id: int):
        pass

    @abstractmethod
    def delete_by_ids(self, invoice_name_list_ids: list[int]):
        pass

    @abstractmethod
    def get_by_id(self, invoice_name_list_id: int) -> InvoiceNameList:
        pass

    @abstractmethod
    def get_all(self, invoice_id: int) -> list[InvoiceNameList]:
        pass

    @abstractmethod
    def get_all_by_date(self, start_date: date, end_date: date) -> list[InvoiceNameList]:
        pass