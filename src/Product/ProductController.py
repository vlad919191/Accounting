from src.__Parents.Controller import Controller
from .ProductRepository import ProductRepository
from .ProductService import ProductService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .ProductValidator import product_schema
from ..FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from ..ProductType.ProductTypeRepository import ProductTypeRepository
from ..Storage.StorageRepository import StorageRepository
from ..Unit.UnitRepository import UnitRepository
from ..Expense.ExpenseRepository import ExpenseRepository
from ..ExpenseType.ExpenseTypeRepository import ExpenseTypeRepository
from ..Income.IncomeRepository import IncomeRepository
from ..IncomeType.IncomeTypeRepository import IncomeTypeRepository
from ..Colleague.ColleagueRepository import ColleagueRepository


class ProductController(Controller):
    product_service: ProductService = ProductService(ProductRepository(),
                                                     ProductTypeRepository(),
                                                     StorageRepository(),
                                                     UnitRepository(),
                                                     ExpenseRepository(),
                                                     ExpenseTypeRepository(),
                                                     IncomeRepository(),
                                                     IncomeTypeRepository(),
                                                     ColleagueRepository())

    # POST
    @expects_json(product_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('product_edit', firm_request=False)
    def post(self) -> dict:
        res: dict = self.product_service.create(body=self.request.get_json())
        return res

    # PUT
    @expects_json(product_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('product_edit', firm_request=False)
    def put(self) -> dict:
        res: dict = self.product_service.update(product_id=self.id,
                                                body=self.request.get_json())
        return res

    # PATH
    @expects_json()
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('product_edit', firm_request=False)
    def patch(self) -> dict:
        res: dict = self.product_service.sale(product_id=self.id,
                                              body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('product_edit')
    def delete(self) -> dict:
        res: dict = self.product_service.delete(product_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('product_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.product_service.get_by_id(product_id=self.id)
        else:
            res: dict = self.product_service.get_all(
                page=self.page,
                per_page=self.per_page,
                product_type_id=self.arguments.get('product_type_id'),
                storage_id=self.arguments.get('storage_id'),
                search=self.arguments.get('search'))

        return res
