import datetime
from datetime import timedelta
from src.Auth.IAuthModel import IAuthModel
from src.__Parents.Repository import Repository
from .AuthModel import Auth
from src import app
from flask_jwt_extended import create_access_token, create_refresh_token
import jwt


class AuthRepository(Repository, IAuthModel):

    def generate_tokens(self, user_id: int):
        auth: Auth = Auth.query.filter_by(user_id=user_id).first() or Auth(user_id)
        auth.access_token = jwt.encode({'user_id': user_id}, app.config['JWT_SECRET_KEY'], app.config['JWT_ALGORITHM'])
        auth.update_db() or auth.save_db()
        return {'access_token': auth.access_token}

    def get_by_user_id(self, user_id: int):
        auth: Auth = Auth.query.filter_by(user_id=user_id).first()
        if auth.user_role_firm:
            auth.user_role_firm = auth.user_role_firm
            auth.user_role_firm.role = auth.user_role_firm.role
            auth.user_role_firm.role.permissions = auth.user_role_firm.role.permissions
            auth.user_role_firm.role.firm_permissions = auth.user_role_firm.role.firm_permissions
        return self.get_dict_items(auth)

    def update_setting(self, auth_id: int or None, body: dict, user_id: int or None):
        auth: Auth = Auth.query.filter(Auth.id == auth_id if auth_id else Auth.user_id == user_id).first()
        if auth:
            auth.user_role_firm_id = body['user_role_firm_id']
            auth.update_db()




