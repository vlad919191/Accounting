from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IColleagueRepo import IColleagueRepo
from flask import g

from ..Address.IAddressRepo import IAddressRepo


class ColleagueService(Service, Repository):

    def __init__(self, colleague_repository: IColleagueRepo, address_repository: IAddressRepo):
        self.colleague_repository: IColleagueRepo = colleague_repository
        self.address_repository: IAddressRepo = address_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.colleague_repository.get_by_title(title=body['title'], client_id=g.user.client_id):
            return self.response_conflict('название занято')

        colleague = self.colleague_repository.create(body, g.user.client_id)
        self.address_repository.create(addresses=body['addresses'], company_id=colleague.id)
        return self.response_created('коллега создано')

    # UPDATE
    def update(self, colleague_id: int, body: dict) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        addressees = self.address_repository.get_all(company_id=colleague_id)
        self.colleague_repository.update(colleague=colleague, body=body)
        self.address_repository.update(address_models=addressees, addresses_body=body['addresses'])
        return self.response_updated('коллега обновлено')

    # DELETE
    def delete(self, colleague_id: int) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        try:
            self.address_repository.delete_all(colleague.id)
            self.colleague_repository.delete(colleague)
        except:
            return self.response_forbidden('объект нельзя удалить так как к нему ссылаются другие объекты')

        return self.response_deleted('коллега удалено')

    # GET BY ID
    def get_by_id(self, colleague_id: int) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        return self.response_ok({
            "title": colleague.title,
            "code": colleague.code,
            "hvhh": colleague.hvhh,
            "addresses": self.get_array_items(colleague.addresses)
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, search: str or None, firm_id: int or None) -> dict:
        colleagues = self.colleague_repository.get_all(
            page=page,
            per_page=per_page,
            search=search,
            firm_id=firm_id,
            client_id=g.user.client_id)

        return self.response_ok(colleagues)
    