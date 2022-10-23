from src.__Parents.Controller import Controller
from .AuthService import AuthService
from .AuthRepository import AuthRepository
from ..User.UserRepository import UserRepository
from flask_jwt_extended import jwt_required
from .AuthMiddleware import AuthMiddleware
from src.UserRoleFirm.UserRoleFirmRepository import UserRoleFirmRepository


class AuthController(Controller):
    auth_service: AuthService = AuthService(auth_repository=AuthRepository(),
                                            user_repository=UserRepository(),
                                            user_role_firm_repository=UserRoleFirmRepository())

    def post(self):
        return self.auth_service.login(

            body=self.request.get_json()
        )

    @jwt_required(refresh=True)
    def put(self):
        return self.auth_service.refresh()

    @AuthMiddleware.check_authorize
    def patch(self) -> dict:
        res: dict = self.auth_service.setting(body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def get(self):
        return self.auth_service.get_profile()
