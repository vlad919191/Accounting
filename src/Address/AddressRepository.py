from .IAddressRepo import IAddressRepo
from .AddressModel import Address
from flask import g


class AddressRepository(IAddressRepo):

    def create(self, addresses: list[dict], company_id: int):
        address_models: list[Address] = []
        for address_body in addresses:
            address: Address = Address()
            address.activity_address = address_body['activity_address']
            address.account_number = address_body['account_number']

            address.phone_number = address_body['phone_number']
            address.legal_address = address_body['legal_address']
            address.colleague_id = company_id
            address.client_id = g.client_id
            address_models.append(address)

        Address.save_all_db(address_models)

    def update(self, address_models: list[Address], addresses_body: list[dict]):
        for address_model in address_models:
            for address_body in addresses_body:
                if address_body['id'] == address_model.id:
                    address_model.legal_address = address_body['legal_address']
                    address_model.activity_address = address_body['activity_address']

                    address_model.phone_number = address_body['phone_number']
                    address_model.account_number = address_body['account_number']
                    address_model.update_db()
        Address.update_db()

    def delete(self, address: Address):
        address.delete_db()

    def get_by_id(self, address_id: int):
        address = Address.query.filter_by(id=address_id, client_id=g.client_id).first()
        return address

    def get_all(self, company_id: int) -> list[Address]:
        addressees: list[Address] = Address.query.filter_by(colleague_id=company_id, client_id=g.client_id).all()
        return addressees

    def delete_all(self, company_id: int):
        Address.query.filter_by(company_id=company_id, client_id=g.client_id).delete()
