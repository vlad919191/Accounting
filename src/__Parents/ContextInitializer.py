from src import logger
from src.FirmPermission.FirmPermissionRepository import FirmPermissionRepository
from src.FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from src.Permission.IPermissionRepo import IPermissionRepo
from src.User.UserRepository import UserRepository
from src.User.IUserRepo import IUserRepo
from src.Permission.PermissionRepository import PermissionRepository
from src.Client.ClientRepository import ClientRepository
from src.Client.IClientRepo import IClientRepo
from src.__Parents.Service import Service
from src.Role.RoleRepository import RoleRepository
from src.Role.IRoleRepo import IRoleRepo
from src.UserRoleFirm.UserRoleFirmRepository import UserRoleFirmRepository
from src.UserRoleFirm.IUserRoleFirmRepo import IUserRoleFirmRepo


class ContextInitializer(Service):
    user_repository: IUserRepo = UserRepository()
    client_repository: IClientRepo = ClientRepository()
    permission_repository: IPermissionRepo = PermissionRepository()
    role_repository: IRoleRepo = RoleRepository()
    firm_permission_repository: IFirmPermissionRepo = FirmPermissionRepository()
    user_role_firm_repository: IUserRoleFirmRepo = UserRoleFirmRepository()

    # USER
    permissions: list[dict] = [{'name': 'user_get', 'title': 'получить пользователей'},
                               {'name': 'user_edit', 'title': 'редактировать пользователей'},
                               # CLIENT
                               {'name': 'client_get', 'title': 'получить клиентов'},
                               {'name': 'client_edit', 'title': 'редактировать клиентов'},
                               # FIRM
                               {'name': 'firm_edit', 'title': 'редактировать фирмы'},
                               # SPHERE
                               {'name': 'sphere_edit', 'title': 'редактировать сферу'},
                               # POSITION
                               {'name': 'position_edit', 'title': 'редактировать позицию'},
                               # PRODUCT TYPE
                               {'name': 'product_type_edit', 'title': 'редактировать тип продукта'},
                               # UNIT
                               {'name': 'unit_edit', 'title': 'редактировать Единицу измерения '},
                               # INCOME TYPE
                               {'name': 'income_type_edit', 'title': 'редактировать тип прибыли '},
                               # EXPENSE TYPE
                               {'name': 'expense_type_edit', 'title': 'редактировать тип расходов '},
                               # COLLEAGUE
                               {'name': 'colleague_edit', 'title': 'редактировать колег'},
                               {'name': 'colleague_get', 'title': 'получить колег'},
                               # SERVICE
                               {'name': 'service_edit', 'title': 'редактировать услуги'},
                               {'name': 'service_get', 'title': 'получить услуги'},
                               # ROLE
                               {'name': 'role_edit', 'title': 'редактировать роли'},
                               {'name': 'role_get', 'title': 'получить роли'}]
                               # # FIRM ROLE
                               # {'name': 'firm_role_edit', 'title': 'редактировать роли компании'},
                               # {'name': 'firm_role_get', 'title': 'получить роли компании'}]

    firm_permissions: dict = [{'name': 'product_edit', 'title': 'редактировать продукт'},
                              {'name': 'product_get', 'title': 'получить продукт'},

                              {'name': 'storage_edit', 'title': 'редактировать хранилище'},
                              {'name': 'storage_get', 'title': 'получить хранилище'},

                              {'name': 'employee_edit', 'title': 'редактировать работников'},
                              {'name': 'employee_get', 'title': 'получить работников'},

                              {'name': 'resource_edit', 'title': 'редактировать ресурсы'},
                              {'name': 'resource_get', 'title': 'получить ресурсы'},

                              {'name': 'income_edit', 'title': 'редактировать прибыль'},
                              {'name': 'income_get', 'title': 'получить прибыль'},

                              {'name': 'expense_edit', 'title': 'редактировать трату'},
                              {'name': 'expense_get', 'title': 'получить трату'},

                              {'name': 'invoice_edit', 'title': 'Հաշիվ-ապրանքագիր խմբագրել'},
                              {'name': 'invoice_get', 'title': 'Հաշիվ-ապրանքագիր ստանալ'},

                              {'name': 'firm_provision_edit', 'title': 'Կազմակերպության դրույթներ խմբագրել'},
                              {'name': 'firm_provision_get', 'title': 'Կազմակերպության դրույթներ ստանալ'},

                              {'name': 'invoice_statistic_get', 'title': 'получить статистику счетов'}]

    user: dict = {'first_name': '_Admin', 'last_name': 'Adminyan', 'email_address': 'e.pargevich@mail.ru', 'position_id': None}
    client: dict = {'name': 'First client', 'description': 'First client'}
    role: dict = {'name': 'DevAdmin', "description": ""}

    def __init__(self):
        client = self.client_init()
        permissions = self.permissions_init()
        firm_permissions = self.firm_permissions_init()
        role = self.role_init(client_id=client.id, permissions=permissions, firm_permissions=firm_permissions)

        user = self.user_init(client_id=client.id, role_id=role.id)

    # ROLE INITIALIZER
    def role_init(self, client_id: int, permissions: list, firm_permissions: list):
        role = self.role_repository.get_first(client_id)
        if not role:
            self.role_repository.create(body=self.role, client_id=client_id, permissions=permissions, creator_id=None, firm_permissions=firm_permissions)
            return self.role_repository.get_first(client_id)
        return role

    # CLIENT INITIALIZER
    def client_init(self):
        client = self.client_repository.get_by_name(self.client['name'], parent_id=None)
        if not client:
            client = self.client_repository.create(body=self.client, parent_id=None)
            logger.info(f"клиент успешно создан")
        return client

    # USER INITIALIZER
    def user_init(self, client_id, role_id):
        user = self.user_repository.get_by_first_client_id(client_id)

        if not user:
            self.user['role_id'] = role_id
            self.user['ticket'] = self.generate_ticket_code()
            user = self.user_repository.create(body=self.user, client_id=client_id)
            self.user_firm_role_init(user_id=user.id, role_id=role_id)
            logger.info(f"первый пользователь создан, код регистрации {user.ticket}")

        return user

    # PERMISSIONS INITIALIZER
    def permissions_init(self):
        for permission_dict in self.permissions:
            permission = self.permission_repository.get_by_name(permission_dict['name'])
            if not permission:
                permission = self.permission_repository.create(name=permission_dict['name'], title=permission_dict['title'])
                logger.info(f"разрешение по названию {permission.title} успешно создан ")

        permissions = self.permission_repository.get_all()
        return permissions

    def firm_permissions_init(self):
        if not len(self.firm_permission_repository.get_all()):
            self.firm_permission_repository.create(self.firm_permissions)

        return self.firm_permission_repository.get_all()

    def user_firm_role_init(self, user_id: int, role_id: int):
        self.user_role_firm_repository.create(user_id=user_id, role_id=role_id, firm_id=None)
