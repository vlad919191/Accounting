from functools import wraps
from flask import g, request
from src.Permission.PermissionRepository import PermissionRepository
from src.__Parents.Service import Service


class PermissionMiddleware(Service):
    permission_repository = PermissionRepository()

    @staticmethod
    def check_permission(permission_name):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                if g.roles:
                    for role in g.roles:
                        if len(role.permissions):
                            for permission in role.permissions:
                                if permission.name == permission_name:
                                    return f(*args, **kwargs)

                return PermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
