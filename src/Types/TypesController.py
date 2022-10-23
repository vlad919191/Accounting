from src.__Parents.Controller import Controller
from src.Auth.AuthMiddleware import AuthMiddleware
from .TypesService import TypesService
from src.Unit.UnitRepository import UnitRepository
from src.ExpenseType.ExpenseTypeRepository import ExpenseTypeRepository
from src.IncomeType.IncomeTypeRepository import IncomeTypeRepository
from src.ProductType.ProductTypeRepository import ProductTypeRepository
from src.InvoiceType.InvoiceTypeRepository import InvoiceTypeRepository
from ..Sphere.SpeheRepository import SphereRepository


class TypesController(Controller):
    types_service: TypesService = TypesService(
        unit_repository=UnitRepository(),
        income_type_repository=IncomeTypeRepository(),
        expense_type_repository=ExpenseTypeRepository(),
        product_type_repository=ProductTypeRepository(),
        sphere_repository=SphereRepository(),
        invoice_type_repository=InvoiceTypeRepository()
    )

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.types_service.get_all()
        return res
