from .IInvoiceRepo import IInvoiceRepo
from .InvoiceModel import Invoice
from flask import g
from src.__Parents.Repository import Repository


class InvoiceRepository(IInvoiceRepo, Repository):
    def create(self, body: dict):
        invoice: Invoice = Invoice()

        invoice.title = body['title']
        invoice.date = body['date'].split("T")[0]
        invoice.document_number = body['document_number']
        invoice.buyer_account = body['buyer_account']

        invoice.bar_code = body['bar_code']
        invoice.contract = body['contract']
        invoice.contact_date = body['contact_date'].split("T")[0]
        invoice.prepaid_account = body['prepaid_account']

        invoice.aah_account = body['aah_account']
        invoice.out_type = body['out_type']

        invoice.series_and_number = body['series_and_number']
        invoice.out_date = body['out_date'].split("T")[0]
        invoice.description = body['description']

        invoice.provider_id = body['provider_id']
        invoice.buyer_id = body['buyer_id']

        invoice.firm_id = g.firm_id
        invoice.client_id = g.client_id
        invoice.save_db()
        return invoice

    def update(self, invoice: Invoice, body: dict):
        invoice.date = body['date'].split("T")[0]
        invoice.title = body['title']
        invoice.document_number = body['document_number']
        invoice.buyer_account = body['buyer_account']

        invoice.bar_code = body['bar_code']
        invoice.contract = body['contract']
        invoice.contact_date = body['contact_date'].split("T")[0]
        invoice.prepaid_account = body['prepaid_account']

        invoice.aah_account = body['aah_account']
        invoice.out_type = body['out_type']

        invoice.series_and_number = body['series_and_number']
        invoice.out_date = body['out_date'].split("T")[0]
        invoice.description = body['description']

        invoice.provider_id = body['provider_id']
        invoice.buyer_id = body['buyer_id']
        invoice.update_db()

    def delete(self, invoice: Invoice):
        invoice.delete_db()

    def get_by_id(self, invoice_id: int) -> Invoice:
        invoice = Invoice.query.filter_by(id=invoice_id, firm_id=g.firm_id).first()
        return invoice

    def get_all(self, page: int, per_page: int):
        invoices = Invoice.query.filter_by(firm_id=g.firm_id).paginate(page=page, per_page=per_page)
        return self.get_page_items(invoices)

    def get_by_document_number(self, document_number: str) -> Invoice:
        invoice = Invoice.query.filter_by(document_number=document_number).first()
        return invoice

    # def create_invoice_name_lists(self, invoice_name_lists: list[dict], invoice_id: int):
    #     for invoice_name_list_dict in invoice_name_lists:
    #         invoice_name_list: InvoiceNameList = InvoiceNameList()
    #         invoice_name_list.type = invoice_name_list_dict['type']
    #         invoice_name_list.storage_id = invoice_name_list_dict['storage_id']
    #         invoice_name_list.unit_id = invoice_name_list_dict['unit_id']
    #         invoice_name_list.price = invoice_name_list_dict['price']
    #         invoice_name_list.count = invoice_name_list_dict['count']
    #         invoice_name_list.invoice_id = invoice_id
    #         invoice_name_list.save_db()
    #
    # def update_invoice_name_lists(self, invoice_name_lists: list[dict], invoice_id: int):
    #     invoice_name_list: list[InvoiceNameList] = InvoiceNameList.query.filter_by(invoice_id=invoice_id).all()
    #
    #     for invoice_name_list_dict in invoice_name_lists:
    #         for invoice_name_list_model in invoice_name_list:
    #             if invoice_name_list_model.id == invoice_name_list_dict['id']:
    #                 invoice_name_list.type = invoice_name_list_dict['type']
    #                 invoice_name_list.storage_id = invoice_name_list_dict['storage_id']
    #                 invoice_name_list.unit_id = invoice_name_list_dict['unit_id']
    #                 invoice_name_list.price = invoice_name_list_dict['price']
    #                 invoice_name_list.count = invoice_name_list_dict['count']
    #                 invoice_name_list.update_db()
