from abc import ABC, abstractmethod
from .AuthRestoreModel import AuthRestore


class IAuthRestoreRepo(ABC):
    @abstractmethod
    def create(self, user_id: int, ticket: str) -> AuthRestore:
        pass

    @abstractmethod
    def update(self, auth_restore: AuthRestore, ticket: str) -> AuthRestore:
        pass

    @abstractmethod
    def delete(self, auth_restore: AuthRestore):
        pass

    @abstractmethod
    def get(self, user_id: int or None, ticket: str or None) -> AuthRestore:
        pass
