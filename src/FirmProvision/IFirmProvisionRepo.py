from abc import ABC, abstractmethod
from .FirmProvisionModel import FirmProvision


class IFirmProvisionRepo(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, firm_provision: FirmProvision, body: dict):
        pass

    @abstractmethod
    def delete(self, firm_provision: FirmProvision):
        pass

    @abstractmethod
    def get_by_id(self, firm_provision_id: int) -> FirmProvision:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int):
        pass
