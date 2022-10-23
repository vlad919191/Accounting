from abc import ABC, abstractmethod
from .IncomeModel import Income


class IIncomeRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, income: Income, body: dict):
        pass

    @abstractmethod
    def delete(self, income: Income):
        pass

    @abstractmethod
    def get_by_id(self, income_id: int) -> Income:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, firm_id: int or None, paid: bool or None) -> dict:
        pass


