from src.__Parents.Service import Service
from src.__Parents.Repository import Repository
from .IInvoiceRepo import IInvoiceRepo
from src.InvoiceNameList.IInvoiceNameListRepo import IInvoiceNameListRepo
from src.Colleague.IColleagueRepo import IColleagueRepo
from src.Storage.IStorageRepo import IStorageRepo
from src.Unit.IUnitRepo import IUnitRepo
from flask import g


class InvoiceService(Service, Repository):

    def __init__(self, invoice_repository: IInvoiceRepo, unit_repository: IUnitRepo, storage_repository: IStorageRepo, colleague_repository: IColleagueRepo,
                 invoice_name_list_repository: IInvoiceNameListRepo):
        self.invoice_repository: IInvoiceRepo = invoice_repository
        self.unit_repository: IUnitRepo = unit_repository
        self.storage_repository: IStorageRepo = storage_repository
        self.colleague_repository: IColleagueRepo = colleague_repository
        self.invoice_name_list_repository: IInvoiceNameListRepo = invoice_name_list_repository

    def create(self, body: dict) -> dict:
        if not self.colleague_repository.get_by_id(colleague_id=body['buyer_id'], client_id=g.client_id):
            return self.response_not_found('colleague not found')

        invoice = self.invoice_repository.create(body)
        for invoice_name_list in body['new_invoice_name_lists']:
            if not self.unit_repository.get_by_id(invoice_name_list['unit_id']):
                return self.response_not_found('unit not found')

            if not self.storage_repository.get_by_id(invoice_name_list['storage_id']):
                return self.response_not_found('storage not found')
            self.invoice_name_list_repository.create(body=invoice_name_list, invoice_id=invoice.id)

        return self.response_created('invoice successfully created')

    def update(self, invoice_id: int, body: dict) -> dict:
        if not self.colleague_repository.get_by_id(colleague_id=body['buyer_id'], client_id=g.client_id):
            return self.response_not_found('colleague not found')

        invoice = self.invoice_repository.get_by_id(invoice_id)
        if not invoice:
            return self.response_not_found('invoice not found')

        if not self.colleague_repository.get_by_id(colleague_id=body['buyer_id'], client_id=g.client_id):
            return self.response_not_found('colleague not found')

        self.invoice_repository.update(invoice=invoice, body=body)
        for invoice_name_list in body['new_invoice_name_lists']:
            if not self.unit_repository.get_by_id(invoice_name_list['unit_id']):
                return self.response_not_found('unit not found')

            if not self.storage_repository.get_by_id(invoice_name_list['storage_id']):
                return self.response_not_found('storage not found')
            self.invoice_name_list_repository.create(body=invoice_name_list, invoice_id=invoice.id)

        return self.response_updated('invoice successfully updated')

    def delete(self, invoice_id: int) -> dict:
        invoice = self.invoice_repository.get_by_id(invoice_id)
        if not invoice:
            return self.response_not_found('invoice not found')
        self.invoice_name_list_repository.delete_all(invoice_id=invoice.id)
        self.invoice_repository.delete(invoice)
        return self.response_deleted('invoice successfully deleted')

    def get_by_id(self, invoice_id: int) -> dict:
        invoice = self.invoice_repository.get_by_id(invoice_id)
        if not invoice:
            return self.response_not_found('invoice not found')

        # invoice.name_lists = self.get_array_items(invoice.name_lists)
        return self.response_ok({
                "aah_account": invoice.aah_account,
                "bar_code": invoice.bar_code,
                "buyer_account": invoice.buyer_account,
                "buyer_id": invoice.buyer_id,
                "contact_date": invoice.contact_date,
                "contract": invoice.contract,
                "date": invoice.date,
                "description": invoice.description,
                "document_number": invoice.document_number,
                "firm_id": invoice.firm_id,
                "id": invoice.id,
                "out_date": invoice.out_date,
                "out_type": invoice.out_type,
                "prepaid_account": invoice.prepaid_account,
                "provider_id": invoice.provider_id,
                "series_and_number": invoice.series_and_number,
                "title": invoice.title,
                "invoice_name_lists": [{
                    'id': invoice_name_list.id,
                    'invoice_type': self.get_dict_items(invoice_name_list.invoice_type),
                    'storage': self.get_dict_items(invoice_name_list.storage),
                    'unit': self.get_dict_items(invoice_name_list.unit),
                    'count': invoice_name_list.count,
                    'price': invoice_name_list.price,
                    'aah': invoice_name_list.aah,
                    'expense_account': invoice_name_list.expense_account,
                    'income_account': invoice_name_list.income_account,
                    'batch': invoice_name_list.batch
                } for invoice_name_list in invoice.invoice_name_lists]
        })

    def get_all(self, page: int, per_page: int) -> dict:
        invoices = self.invoice_repository.get_all(page, per_page)
        return self.response_ok(invoices)

    def get_document_number(self) -> dict:
        generated_number = self.generate_ticket_code(length=16, lowercase=True)
        return self.response_ok({"document_number": generated_number})


