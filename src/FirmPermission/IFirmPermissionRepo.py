from abc import ABC, abstractmethod
from .FirmPermissionModel import FirmPermission


class IFirmPermissionRepo(ABC):

    @abstractmethod
    def create(self, firm_permissions):
        pass

    @abstractmethod
    def get_by_id(self, firm_permission_id: int):
        pass

    @abstractmethod
    def delete(self, firm_id: int):
        pass

    @abstractmethod
    def delete_all_firm_permissions_by_role_id(self, role_id: int):
        pass

    @abstractmethod
    def get_all(self) -> list[FirmPermission]:
        pass

    @abstractmethod
    def get_all_by_user_id(self, user_id: int):
        pass



