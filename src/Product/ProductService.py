from src.__Parents.Service import Service
from .IProductRepo import IProductRepo
from flask import g

from ..Colleague.IColleagueRepo import IColleagueRepo
from ..ExpenseType.IExpenseTypeRepo import IExpenseTypeRepo
from ..Income.IIncomeRepo import IIncomeRepo
from ..IncomeType.IIncomeTypeRepo import IIncomeTypeRepo
from ..ProductType.IProductTypeRepo import IProductTypeRepo
from ..Storage.IStorageRepo import IStorageRepo
from ..Unit.IUnitRepo import IUnitRepo
from ..Expense.IExpenseRepo import IExpenseRepo
from ..__Parents.Repository import Repository


class ProductService(Service, Repository):
    def __init__(self, product_repository: IProductRepo,
                 product_type_repository: IProductTypeRepo,
                 storage_repository: IStorageRepo,
                 unit_repository: IUnitRepo,
                 expense_repository: IExpenseRepo,
                 expense_type_repository: IExpenseTypeRepo,
                 income_repository: IIncomeRepo,
                 income_type_repository: IIncomeTypeRepo,
                 colleague_repository: IColleagueRepo):

        self.product_repository: IProductRepo = product_repository
        self.product_type_repository: IProductTypeRepo = product_type_repository
        self.storage_repository: IStorageRepo = storage_repository
        self.unit_repository: IUnitRepo = unit_repository
        self.expense_repository: IExpenseRepo = expense_repository
        self.expense_type_repository: IExpenseTypeRepo = expense_type_repository
        self.income_repository: IIncomeRepo = income_repository
        self.income_type_repository: IIncomeTypeRepo = income_type_repository
        self.colleague_repository: IColleagueRepo = colleague_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if not self.product_type_repository.get_by_id(product_type_id=body['product_type_id'], client_id=g.client_id):
            return self.response_not_found('тип продукта не найден')

        storage = self.storage_repository.get_by_id(body['storage_id'])
        if not storage:
            return self.response_not_found('хранилище не найдено')

        if not self.unit_repository.get_by_id(body['unit_id']):
            return self.response_not_found('единица измерения не найдена')

        if not self.expense_type_repository.get_by_id(body['expense_type_id']):
            return self.response_not_found('тип траты не найден')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found("коллега не найдена ")

        product = self.product_repository.create(
                  body=body,
                  client_id=g.client_id)

        expense_body = {'title': '',
                        'description': '',
                        'expense_type_id': body['expense_type_id'],
                        'colleague_id': body['colleague_id'],
                        'firm_id': storage.firm_id,
                        'price': body['self_price'] * body['count'],
                        'product_id': product.id,
                        'paid': False}

        self.expense_repository.create(body=expense_body, client_id=g.client_id)
        return self.response_created('продукт создан')

    # UPDATE
    def update(self, product_id: int, body: dict) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        if not self.product_type_repository.get_by_id(product_type_id=body['product_type_id'], client_id=g.client_id):
            return self.response_not_found('тип продукта не найден ')

        if not self.storage_repository.get_by_id(body['storage_id']):
            return self.response_not_found('хранилище не найдено')

        if not self.unit_repository.get_by_id(body['unit_id']):
            return self.response_not_found('единица измерения не найдена')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found("коллега не найдена ")

        storage = self.storage_repository.get_by_id(body['storage_id'])
        if not storage:
            return self.response_not_found('хранилище не найдено')

        expense = self.expense_repository.get_by_product_id(product.id)
        self.product_repository.update(product=product, body=body)

        expense_body = {'title': expense.title,
                        'description': expense.description,
                        'expense_type_id': body['expense_type_id'],
                        'colleague_id': body['colleague_id'],
                        'firm_id': storage.firm_id,
                        'price': body['self_price'] * body['count'],
                        'product_id': product.id,
                        'paid': False}

        self.expense_repository.update(expense=expense, body=expense_body)
        return self.response_updated('продукт обновлен')

    # SALE
    def sale(self, product_id: int, body: dict) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        if not self.income_type_repository.get_by_id(body['income_type_id']):
            return self.response_not_found('тип прибыли не найден')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found("коллега не найдена ")

        if product.count < body['count']:
            return self.response_err_msg('недоступное количество продукта')

        product.count = product.count - body['count']
        product.update_db()

        income_body = {"price": (body['price'] * body['count']) - (product.self_price * body["count"]),
                       "count": body["count"],
                       "product_id": product_id,
                       "colleague_id": body['colleague_id'],
                       "firm_id": product.storage.firm_id,
                       "income_type_id": body["income_type_id"],
                       "paid": False}
        self.income_repository.create(body=income_body, client_id=g.client_id)
        return self.response_created("вывод прошла успешно")

    # DELETE
    def delete(self, product_id: int) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        try:
            self.product_repository.delete(product=product)
        except:
            return self.response_forbidden('объект нельзя удалить так как к нему ссылаются другие объекты')

        return self.response_deleted('продукт удален')

    # GET BY ID
    def get_by_id(self, product_id: int) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        expense = self.expense_repository.get_by_product_id(product.id)
        product.expense_type_id = expense.expense_type_id if expense else None
        product.colleague_id = expense.colleague_id if expense else None

        return self.response_ok(self.get_dict_items(product))

    # GET ALL
    def get_all(self, page: int, per_page: int, search: str or None, product_type_id: int or None, storage_id: int or None) -> dict:
        products = self.product_repository.get_all(
            page=page,
            per_page=per_page,
            product_type_id=product_type_id,
            storage_id=storage_id,
            client_id=g.client_id,
            search=search)

        return self.response_ok(products)
