from abc import ABC, abstractmethod


class IUserRoleFirmRepo(ABC):

    @abstractmethod
    def create(self, user_id: int, role_id: int, firm_id: int or None):
        pass

    @abstractmethod
    def get_all(self, user_id: int or None, role_id: int or None, firm_id: int or None):
        pass

    @abstractmethod
    def get_by_id(self, user_role_firm_id: int, user_id: int or None):
        pass

    @abstractmethod
    def delete_all_by_user_id(self, user_id: int):
        pass

    @abstractmethod
    def delete_all_by_firm_id(self, firm_id: int):
        pass