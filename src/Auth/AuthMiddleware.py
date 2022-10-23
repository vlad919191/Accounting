from functools import wraps
from flask import g, request
import jwt
from src.Auth.AuthRepository import AuthRepository
from src.Auth.IAuthModel import IAuthModel
from src.Role.IRoleRepo import IRoleRepo
from src.Role.RoleRepository import RoleRepository
from src.User.UserRepository import UserRepository
from src.User.IUserRepo import IUserRepo
from src.UserRoleFirm.IUserRoleFirmRepo import IUserRoleFirmRepo
from src.UserRoleFirm.UserRoleFirmRepository import UserRoleFirmRepository
from src.__Parents.Service import Service
from src import app


class AuthMiddleware(Service):
    __auth_repository: IAuthModel = AuthRepository()
    __user_repository: IUserRepo = UserRepository()
    __user_role_firm_repository: IUserRoleFirmRepo = UserRoleFirmRepository()

    @staticmethod
    def check_authorize(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                decode = jwt.decode(request.headers['Authorization'].split(' ')[1],
                                    app.config['JWT_SECRET_KEY'],
                                    algorithms=[app.config['JWT_ALGORITHM']])
            except:
                return AuthMiddleware.response_invalid_login()

            auth = AuthMiddleware.__auth_repository.get_by_user_id(decode['user_id'])
            if decode and auth:
                user = AuthMiddleware.__user_repository.get_by_id(user_id=decode['user_id'], client_id=None)
                g.auth = auth
                g.user = user
                g.roles = user.roles
                g.permissions = auth['user_role_firm']['role']['permissions'] if auth['user_role_firm'] else []
                g.firm_permissions = auth['user_role_firm']['role']['firm_permissions'] if auth['user_role_firm'] else []
                g.firm_id = auth['user_role_firm']['firm_id'] if auth['user_role_firm'] else None

                g.user_id = user.id
                g.client_id = user.client_id

                user_role_firm_list = AuthMiddleware.__user_role_firm_repository.get_all(
                    user_id=g.user.id, firm_id=None, role_id=None)

                g.all_firm_ids = [user_role_firm.firm_id for user_role_firm in user_role_firm_list]
                g.user_role_firm_list = user_role_firm_list

                return f(*args, **kwargs)
            return AuthMiddleware.response_invalid_login()

        return decorated_function

    # @staticmethod
    # def check_authorize(f):
    #     @wraps(f)
    #     @jwt_required()
    #     def decorated_function(*args, **kwargs):
    #
    #         auth = AuthMiddleware.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
    #         if auth['access_token'] == request.headers['authorization'].split(' ')[1]:
    #
    #             if AuthMiddleware.__user_repository.get_by_id(auth['user_id']):
    #                 g.user_id = get_jwt_identity()
    #                 return f(*args, **kwargs)
    #
    #         return Service.response_invalid_login()
    #     return decorated_function

