from functools import wraps
from flask import g, request
from src.FirmPermission.FirmPermissionRepository import FirmPermissionRepository
from src.__Parents.Service import Service
from src.Role.RoleRepository import RoleRepository
from src.Role.IRoleRepo import IRoleRepo


class FirmPermissionMiddleware(Service):
    firm_permission_repository = FirmPermissionRepository()
    role_repository: IRoleRepo = RoleRepository()

    @staticmethod
    def check_permission(permission_name: bool or str = False, firm_request: bool = False):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                allowed_firm_ids: list[int] = []
                g.allowed_firm_ids: list[int] = []

                if g.firm_id and permission_name:
                    for g_firm_permission in g.firm_permissions:

                        if g_firm_permission.name == permission_name and g.firm_id in g.all_firm_ids:
                            allowed_firm_ids.append(g.firm_id)

                if not permission_name:
                    for firm_permission in g.firm_permissions:

                        if permission_name:
                            if permission_name in firm_permission.name:
                                allowed_firm_ids = g.all_firm_ids
                        else:
                            allowed_firm_ids = g.all_firm_ids

                if firm_request:
                    # firm_id: int = int(request.args.get('firm_id') or request.get_json()['firm_id'])
                    firm_id: int = g.firm_id
                    allowed = False
                    if len(g.roles):
                        for firm_permission in g.firm_permissions:
                            if permission_name and firm_permission.name == permission_name and firm_id in g.all_firm_ids:
                                allowed = True
                                break
                    if not allowed:
                        return FirmPermissionMiddleware.response_forbidden('ресурс запрещен')

                if not len(allowed_firm_ids) and not g.firm_id:
                    for user_role_firm in g.user_role_firm_list:
                        for firm_permission in user_role_firm.role.firm_permissions:
                            if firm_permission.name == permission_name:
                                g.allowed_firm_ids.append(user_role_firm.firm_id)
                else:
                    g.allowed_firm_ids = allowed_firm_ids

                return f(*args, **kwargs)

                # for firm_permission in g.user.firm_permissions:
                #     if firm_permission.name == permission_name and firm_permission.firm_id == int(request.args.get('firm_id') or request.get_json()['firm_id']):
                #         return f(*args, **kwargs)

                # return FirmPermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
