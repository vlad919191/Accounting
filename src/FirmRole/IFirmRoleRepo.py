# from abc import ABC, abstractmethod
# from typing import List
# from .FirmRoleModel import FirmRole
#
#
# class IFirmRoleRepo(ABC):
#     @abstractmethod
#     def create(self, body: dict, firm_permissions: list, client_id: int):
#         pass
#
#     @abstractmethod
#     def update(self, firm_role: FirmRole, body: dict, firm_permissions: list):
#         pass
#
#     @abstractmethod
#     def delete(self, firm_role: FirmRole):
#         pass
#
#     @abstractmethod
#     def get_by_id(self, firm_role_id: int) -> FirmRole:
#         pass
#
#     @abstractmethod
#     def get_first(self, client_id) -> FirmRole:
#         pass
#
#     @abstractmethod
#     def get_by_name(self, name: str):
#         pass
#
#     @abstractmethod
#     def get_by_name_exclude_id(self, firm_role_id: int, name: str) -> FirmRole:
#         pass
#
#     @abstractmethod
#     def get_all(self) -> List:
#         pass
#
#     @abstractmethod
#     def get_all_by_ids(self, firm_role_ids: list[int]) -> List[FirmRole]:
#         pass
#
#     # @abstractmethod
#     # def delete_role_permissions_by_role_id(self, role_id: int):
#     #     pass
#     #
#     # @abstractmethod
#     # def delete_all_role_firm_permissions_by_role_id(self, role_id: int):
#     #     pass
#     #
#     # @abstractmethod
#     # def create_user_role_firm(self, user_id: int, role_id: int, firm_id: int):
#     #     pass
#
#     @abstractmethod
#     def cancel(self, role: FirmRole):
#         pass
