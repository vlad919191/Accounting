from abc import ABC, abstractmethod


class IPermissionRepo(ABC):

    @abstractmethod
    def create(self, name: str, title: str):
        pass

    @abstractmethod
    def get_by_id(self, permission_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    # @abstractmethod
    # def delete_user_permissions_by_role_id(self, role_id: int):
    #     pass






