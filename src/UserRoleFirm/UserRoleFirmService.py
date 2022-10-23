from src.UserRoleFirm.IUserRoleFirmRepo import IUserRoleFirmRepo
from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from flask import g


class UserRoleFirmService(Service, Repository):
    def __init__(self, user_role_firm_repository: IUserRoleFirmRepo):
        self.user_role_firm_repository: IUserRoleFirmRepo = user_role_firm_repository

    def get_all(self) -> dict:
        user_role_firms = self.user_role_firm_repository.get_all(user_id=g.user.id, role_id=None, firm_id=None)
        return self.response_ok([{
            'id': user_role_firm.id,
            'role_name': user_role_firm.role.name,
            'firm_title': user_role_firm.firm.title if user_role_firm.firm_id else None
        } for user_role_firm in user_role_firms])
