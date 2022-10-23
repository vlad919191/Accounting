from src.InvoiceType.IInvoiceTypeRepo import IInvoiceTypeRepo
from src.Sphere.ISphereRepo import ISphereRepo
from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from src.Unit.IUnitRepo import IUnitRepo
from src.ExpenseType.IExpenseTypeRepo import IExpenseTypeRepo
from src.IncomeType.IIncomeTypeRepo import IIncomeTypeRepo
from src.ProductType.IProductTypeRepo import IProductTypeRepo
from flask import g


class TypesService(Service, Repository):
    def __init__(self, unit_repository: IUnitRepo,
                 income_type_repository: IIncomeTypeRepo,
                 expense_type_repository: IExpenseTypeRepo,
                 product_type_repository: IProductTypeRepo,
                 sphere_repository: ISphereRepo,
                 invoice_type_repository: IInvoiceTypeRepo):
        self.unit_repository: IUnitRepo = unit_repository
        self.income_type_repository: IIncomeTypeRepo = income_type_repository
        self.expense_type_repository: IExpenseTypeRepo = expense_type_repository
        self.product_type_repository: IProductTypeRepo = product_type_repository
        self.sphere_repository: ISphereRepo = sphere_repository
        self.invoice_type_repository: IInvoiceTypeRepo = invoice_type_repository

    def get_all(self) -> dict:
        return self.response_ok({
            "units": self.unit_repository.get_all(),
            "incomeTypes": self.income_type_repository.get_all(),
            "expenseType": self.expense_type_repository.get_all(),
            "productType": self.product_type_repository.get_all(client_id=g.client_id),
            "sphere": self.sphere_repository.get_all(),
            "invoiceType": self.get_array_items(self.invoice_type_repository.get_all())
        })
