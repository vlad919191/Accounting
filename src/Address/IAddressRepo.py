from abc import ABC, abstractmethod
from .AddressModel import Address


class IAddressRepo(ABC):

    @abstractmethod
    def create(self, addresses: list[dict], company_id: int):
        pass

    @abstractmethod
    def update(self, address_models: list[Address], addresses_body: list[dict]):
        pass

    @abstractmethod
    def delete(self, address: Address):
        pass

    @abstractmethod
    def get_by_id(self, address_id: int):
        pass

    @abstractmethod
    def get_all(self, company_id: int) -> list[Address]:
        pass

    @abstractmethod
    def delete_all(self, company_id: int):
        pass

