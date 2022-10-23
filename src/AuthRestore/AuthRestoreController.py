from .AuthRestoreService import AuthRestoreService
from .AuthRestoreRepository import AuthRestoreRepository
from src.User.UserRepository import UserRepository
from ..__Parents.Controller import Controller
from flask_expects_json import expects_json
from .AuthRestoreValidator import create_auth_restore_schema, auth_restore_schema


class AuthRestoreController(Controller):
    auth_restore_service: AuthRestoreService = AuthRestoreService(AuthRestoreRepository(), UserRepository())

    @expects_json(create_auth_restore_schema)
    def post(self) -> dict:
        res: dict = self.auth_restore_service.create(self.request.get_json())
        return res

    @expects_json(auth_restore_schema)
    def put(self) -> dict:
        res: dict = self.auth_restore_service.restore(self.request.get_json())
        return res
