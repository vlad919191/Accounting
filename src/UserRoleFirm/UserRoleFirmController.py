from src.__Parents.Controller import Controller
from .UserRoleFirmService import UserRoleFirmService
from .UserRoleFirmRepository import UserRoleFirmRepository
from src.Auth.AuthMiddleware import AuthMiddleware


class UserRoleFirmController(Controller):
    user_role_firm_service: UserRoleFirmService = UserRoleFirmService(UserRoleFirmRepository())

    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        res: dict = self.user_role_firm_service.get_all()
        return res

