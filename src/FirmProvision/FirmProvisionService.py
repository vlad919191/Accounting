from .IFirmProvisionRepo import IFirmProvisionRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class FirmProvisionService(Service, Repository):

    def __init__(self, firm_provision_repository: IFirmProvisionRepo):
        self.firm_provision_repository: IFirmProvisionRepo = firm_provision_repository

    def create(self, body: dict) -> dict:
        self.firm_provision_repository.create(body)
        return self.response_created('firm provision successfully created')

    def update(self, firm_provision_id: int, body: dict) -> dict:
        firm_provision = self.firm_provision_repository.get_by_id(firm_provision_id)
        if not firm_provision:
            return self.response_not_found('firm provision not found')

        self.firm_provision_repository.update(firm_provision, body)
        return self.response_updated('firm provision successfully updated')

    def delete(self, firm_provision_id: int) -> dict:
        firm_provision = self.firm_provision_repository.get_by_id(firm_provision_id)
        if not firm_provision:
            return self.response_not_found('firm provision not found')

        self.firm_provision_repository.delete(firm_provision)
        return self.response_deleted('firm provision successfully deleted')

    def get_by_id(self, firm_provision_id: int) -> dict:
        firm_provision = self.firm_provision_repository.get_by_id(firm_provision_id)
        if not firm_provision:
            return self.response_not_found('firm provision not found')
        return self.response_ok(self.get_dict_items(firm_provision))

    def get_all(self, page: int, per_page: int) -> dict:
        firm_provisions = self.firm_provision_repository.get_all(page, per_page)
        return self.response_ok(firm_provisions)
