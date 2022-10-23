from sqlalchemy import and_

from .IInvoiceNameListRepo import IInvoiceNameListRepo
from .InvoiceNameListModel import InvoiceNameList
from flask import g
from datetime import datetime, date


class InvoiceNameListRepository(IInvoiceNameListRepo):
    def create(self, body: dict, invoice_id: int):
        invoice_name_list: InvoiceNameList = InvoiceNameList()
        invoice_name_list.invoice_type_id = body['invoice_type_id']
        invoice_name_list.storage_id = body['storage_id']
        invoice_name_list.unit_id = body['unit_id']
        invoice_name_list.count = body['count']
        invoice_name_list.price = body['price']

        invoice_name_list.aah = body['aah'] == 'true'
        invoice_name_list.expense_account = body['expense_account']
        invoice_name_list.income_account = body['income_account']
        invoice_name_list.batch = body['batch']
        invoice_name_list.invoice_id = invoice_id
        invoice_name_list.firm_id = g.firm_id
        invoice_name_list.client_id = g.client_id
        invoice_name_list.save_db()

    def update(self, invoice_name_list: InvoiceNameList, body: dict):
        invoice_name_list.invoice_type_id = body['invoice_type_id']
        invoice_name_list.storage_id = body['storage_id']

        invoice_name_list.unit_id = body['unit_id']
        invoice_name_list.count = body['count']
        invoice_name_list.price = body['price']

        invoice_name_list.aah = body['aah'] == 'true'
        invoice_name_list.expense_account = body['expense_account']
        invoice_name_list.income_account = body['income_account']
        invoice_name_list.batch = body['batch']
        invoice_name_list.update_db()

    def delete(self, invoice_name_list: InvoiceNameList):
        invoice_name_list.delete_db()

    def delete_all(self, invoice_id: int):
        InvoiceNameList.query.filter_by(invoice_id=invoice_id, firm_id=g.firm_id, client_id=g.client_id).delete()

    def delete_by_ids(self, invoice_name_list_ids: list[int]):
        InvoiceNameList.query.filter_by(firm_id=g.firm_id).filter(InvoiceNameList.id.in_(invoice_name_list_ids)).delete()

    def get_by_id(self, invoice_name_list_id: InvoiceNameList) -> InvoiceNameList:
        invoice_name_list: InvoiceNameList = InvoiceNameList.query.filter_by(
            id=invoice_name_list_id,
            firm_id=g.firm_id,
            client_id=g.client_id).first()
        return invoice_name_list

    def get_all(self, invoice_id: int) -> list[InvoiceNameList]:
        name_lists: list[InvoiceNameList] = InvoiceNameList.query.filter_by(
            invoice_id=invoice_id,
            firm_id=g.firm_id,
            client_id=g.client_id).all()
        return name_lists

    def get_all_by_date(self, start_date: date, end_date: date) -> list[InvoiceNameList]:
        name_lists: list[InvoiceNameList] = InvoiceNameList.query\
            .filter(InvoiceNameList.firm_id.in_(g.allowed_firm_ids))\
            .filter(InvoiceNameList.creation_date >= start_date)\
            .filter(InvoiceNameList.creation_date <= end_date).all()
        return name_lists
