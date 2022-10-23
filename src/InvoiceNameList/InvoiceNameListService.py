from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IInvoiceNameListRepo import IInvoiceNameListRepo
from datetime import datetime, date


class InvoiceNameListService(Service, Repository):

    def __init__(self, invoice_name_list_repository: IInvoiceNameListRepo):
        self.invoice_name_list_repository: IInvoiceNameListRepo = invoice_name_list_repository

    # def create(self, body: dict) -> dict:
    #     invoice_name_list = self.invoice_name_list_repository.create(body)
    #     return self.response_ok(self.get_dict_items(invoice_name_list))

    def update(self, invoice_name_list_id: int, body: dict) -> dict:
        invoice_name_list = self.invoice_name_list_repository.get_by_id(invoice_name_list_id)
        if not invoice_name_list:
            return self.response_not_found('список имен отчета не найден')
        self.invoice_name_list_repository.update(
            invoice_name_list=invoice_name_list,
            body=body)
        return self.response_updated('список имен отчета обновлен')

    def delete(self, invoice_name_list_id: int) -> dict:
        invoice_name_list = self.invoice_name_list_repository.get_by_id(invoice_name_list_id)
        if not invoice_name_list:
            return self.response_not_found('список имен отчета не найден')
        self.invoice_name_list_repository.delete(invoice_name_list)
        return self.response_deleted('список имен отчета удалён')

    def get_all_by_date(self, start_date: date, end_date: date) -> dict:
        invoice_name_lists: list = self.invoice_name_list_repository.get_all_by_date(
            start_date=start_date,
            end_date=end_date)
        return self.response_ok([{
            'creation_date': invoice_name_list.creation_date,
            'price': invoice_name_list.price,
            'firm_id': invoice_name_list.firm_id
        } for invoice_name_list in invoice_name_lists])

    # def get_by_id(self, invoice_name_list_id: int) -> dict:
    #     invoice_name_list = self.invoice_name_list_repository.get_by_id(invoice_name_list_id)
    #     if not invoice_name_list:
    #         return self.response_not_found('список имен отчета не найден')
    #     return self.response_ok(self.get_dict_items(invoice_name_list))
    #
    # def get_all(self, invoice_id: int) -> dict:
    #     invoice_name_lists = self.invoice_name_list_repository.get_all(invoice_id)
    #     return self.response_ok(self.get_array_items(invoice_name_lists))
