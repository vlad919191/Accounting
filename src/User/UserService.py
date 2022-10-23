from .IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from ..Permission.IPermissionRepo import IPermissionRepo
from ..Position.IPositionRepo import IPositionRepo
from ..Role.IRoleRepo import IRoleRepo
from ..UserRoleFirm.IUserRoleFirmRepo import IUserRoleFirmRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from ..FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from flask import g
from src.Auth.IAuthModel import IAuthModel


class UserService(Service, Repository):
    def __init__(self,
                 user_repository: IUserRepo,
                 position_repository: IPositionRepo,
                 user_role_firm_repository: IUserRoleFirmRepo,
                 auth_repository: IAuthModel):

        self._user_repository: IUserRepo = user_repository
        self.position_repository: IPositionRepo = position_repository
        self.user_role_firm_repository: IUserRoleFirmRepo = user_role_firm_repository
        self.auth_repository: IAuthModel = auth_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self._user_repository.get_by_email_address(body['email_address']):
            return self.response_conflict('аддресс электронной почты существует в системе')

        if not self.position_repository.get_by_id(body['position_id']):
            return self.response_not_found('позиция не найдена')

        body['ticket'] = self.generate_ticket_code()
        user = self._user_repository.create(
            body=body,
            client_id=g.client_id)

        for role in body['roles']:
            self.user_role_firm_repository.create(user_id=user.id, role_id=role['role_id'], firm_id=role['firm_id'])

        return self.response_ok({'first_name': user.first_name,
                                 'last_name': user.last_name,
                                 'ticket': user.ticket,
                                 'position': user.position.title or None,
                                 'email_address': user.email_address,
                                 'id': user.id})

    # UPDATE
    def update(self, user_id: int, body: dict) -> dict:
        user = self._user_repository.get_by_id(user_id, client_id=g.client_id)
        if not user:
            return self.response_not_found('пользователь не найден')

        if not self.position_repository.get_by_id(body['position_id']):
            return self.response_not_found('позиция не найдена')

        if self._user_repository.get_by_email_address_exclude_id(user_id=user_id, email_address=body['email_address']):
            return self.response_conflict('аддресс электронной почты существует в системе')

        self._user_repository.update(
            user_id=user_id,
            body=body,
            client_id=g.client_id)

        self.auth_repository.update_setting(user_id=user.id, body={'user_role_firm_id': None}, auth_id=None)
        self.user_role_firm_repository.delete_all_by_user_id(user.id)
        for role in body['roles']:
            self.user_role_firm_repository.create(user_id=user.id, role_id=role['role_id'], firm_id=role['firm_id'])

        return self.response_updated('данные пользователя успешно обновлены')

    # REGISTRATION
    def registration(self, body: dict) -> dict:
        user = self._user_repository.get_by_ticket(ticket=body['ticket'])
        if not user:
            return self.response_not_found('тикет код не найден')

        if self._user_repository.get_by_name(name=body['name']):
            return self.response_conflict('пользователь с таким  именем существует')

        self._user_repository.update_auth(user_id=user.id, body=body)
        return self.response_updated('регстрация прошла успешно')

    # DELETE
    def delete(self, user_id: int):
        user = self._user_repository.get_by_id(user_id, client_id=g.client_id)

        if not user:
            return self.response_not_found('пользователь не найден')

        self.auth_repository.update_setting(user_id=user_id, body={'user_role_firm_id': None}, auth_id=None)
        self.user_role_firm_repository.delete_all_by_user_id(user_id)
        self._user_repository.delete(user_id=user_id, client_id=g.client_id)
        return self.response_deleted('пользователь удален')

    # GET BY ID
    def get_by_id(self, user_id: int) -> dict:
        user = self._user_repository.get_by_id(user_id, client_id=g.client_id)
        if not user:
            return self.response_not_found('пользователь не найден')
        return self.response_ok({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email_address': user.email_address,
            'image_path': user.image_path,
            'ticket': user.ticket,
            'position': self.get_dict_items(user.position),
            'roles': [{
                'role': {
                    'id': user_firm_role.role.id,
                    'name': user_firm_role.role.name
                },
                'firm': {
                    'id': user_firm_role.firm.id,
                    'title': user_firm_role.firm.title
                } if user_firm_role.firm else None
            } for user_firm_role in self.user_role_firm_repository.get_all(user_id=user.id, role_id=None, firm_id=None)],
            'client_id': user.client_id
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, search: str or None, position_id: int or None) -> dict:
        user_list: dict = self._user_repository.get_all(
            page=page,
            per_page=per_page,
            position_id=position_id,
            search=search,
            client_id=g.client_id)
        return self.response_ok(user_list)

