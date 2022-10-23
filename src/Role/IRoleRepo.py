from abc import ABC, abstractmethod
from typing import List

from .RoleModel import Role


class IRoleRepo(ABC):
    @abstractmethod
    def create(self, body: dict, permissions: list, firm_permissions: list, client_id: int, creator_id: int or None,):
        pass

    @abstractmethod
    def update(self, role: Role, body: dict, permissions: list, firm_permissions: list):
        pass

    @abstractmethod
    def delete(self, role: Role):
        pass

    @abstractmethod
    def get_by_id(self, role_id: int) -> Role:
        pass

    @abstractmethod
    def get_first(self, client_id) -> Role:
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, role_id: int, name: str) -> Role:
        pass

    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def get_all_by_ids(self, role_ids: list[int]) -> List[Role]:
        pass

    #
    # @abstractmethod
    # def delete_role_permissions_by_role_id(self, role_id: int):
    #     pass
    #
    # @abstractmethod
    # def delete_all_role_firm_permissions_by_role_id(self, role_id: int):
    #     pass

    @abstractmethod
    def cancel(self, role: Role):
        pass
