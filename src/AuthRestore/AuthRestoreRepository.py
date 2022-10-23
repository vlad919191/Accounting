from .IAuthRestoreRepo import IAuthRestoreRepo
from .AuthRestoreModel import AuthRestore


class AuthRestoreRepository(IAuthRestoreRepo):

    def create(self, user_id: int, ticket: str) -> AuthRestore:
        auth_restore: AuthRestore = AuthRestore()
        auth_restore.ticket = ticket
        auth_restore.user_id = user_id
        auth_restore.save_db()
        return auth_restore

    def update(self, auth_restore: AuthRestore, ticket: str) -> AuthRestore:
        auth_restore.ticket = ticket
        auth_restore.update_db()
        return auth_restore

    def delete(self, auth_restore: AuthRestore):
        auth_restore.delete_db()

    def get(self, user_id: int or None, ticket: str or None) -> AuthRestore:
        auth_restore: AuthRestore = AuthRestore.query.filter(
            AuthRestore.user_id == user_id if user_id else AuthRestore.ticket == ticket
        ).first()
        return auth_restore
