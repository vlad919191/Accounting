from src import api
from .User.UserController import UserController
from .Auth.AuthController import AuthController
from .AuthRestore.AuthRestoreController import AuthRestoreController
from .Client.ClientController import ClientController
from .Firm.FirmController import FirmController
from .Sphere.SphereController import SphereController
from .Position.PositionController import PositionController
from .ProductType.ProductTypeController import ProductTypeController
from .Product.ProductController import ProductController
from .Storage.StorageController import StorageController
from .Unit.UnitController import UnitController
from .IncomeType.IncomeTypeController import IncomeTypeController
from .ExpenseType.ExpenseTypeController import ExpenseTypeController
from .Colleague.ColleagueController import ColleagueController
from .Service.ServiceController import ServiceController
from .Resource.ResourceController import ResourceController
from .Employee.EmployeeController import EmployeeController
from .Income.IncomeController import IncomeController
from .Expense.ExpenseController import ExpenseController
from .Types.TypesController import TypesController
from .Role.RoleController import RoleController
from .Invoice.InvoiceController import InvoiceController
from .InvoiceNameList.InvoiceNameListController import InvoiceNameListController
from .InvoiceType.InvoiceTypeController import InvoiceTypeController
from .FirmProvision.FirmProvisionController import FirmProvisionController
from .UserRoleFirm.UserRoleFirmController import UserRoleFirmController

api.add_resource(AuthController, "/auth")
api.add_resource(AuthRestoreController, "/auth_restore")
api.add_resource(UserController, "/user")
api.add_resource(ClientController, "/client")
api.add_resource(FirmController, "/firm")
api.add_resource(SphereController, "/sphere")
api.add_resource(PositionController, "/position")
api.add_resource(ProductTypeController, "/product_type")
api.add_resource(ProductController, "/product")
api.add_resource(StorageController, "/storage")
api.add_resource(UnitController, "/unit")
api.add_resource(IncomeTypeController, "/income_type")
api.add_resource(ExpenseTypeController, "/expense_type")
api.add_resource(ColleagueController, "/colleague")
api.add_resource(ServiceController, "/service")
api.add_resource(ResourceController, "/resource")
api.add_resource(EmployeeController, "/employee")
api.add_resource(IncomeController, "/income")
api.add_resource(ExpenseController, "/expense")
api.add_resource(TypesController, "/types")
api.add_resource(RoleController, "/role")
api.add_resource(InvoiceController, '/invoice')
api.add_resource(InvoiceNameListController, '/invoice_name_list')
api.add_resource(InvoiceTypeController, '/invoice_type')
api.add_resource(FirmProvisionController, '/firm_provision')
api.add_resource(UserRoleFirmController, '/user_role_firm')
