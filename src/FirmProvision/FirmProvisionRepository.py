from .FirmProvisionModel import FirmProvision
from .IFirmProvisionRepo import IFirmProvisionRepo
from ..__Parents.Repository import Repository
from flask import g


class FirmProvisionRepository(IFirmProvisionRepo, Repository):

    def create(self, body: dict):
        firm_provision: FirmProvision = FirmProvision()
        firm_provision.title = body['title']
        firm_provision.email_address = body['email_address']
        firm_provision.activity_address = body['activity_address']
        firm_provision.legal_address = body['legal_address']
        firm_provision.phone_number = body['phone_number']

        firm_provision.hvhh = body['hvhh']
        firm_provision.chapter_registration_number = body['chapter_registration_number']
        firm_provision.tax_area_code = body['tax_area_code']
        firm_provision.insurer_account_number = body['insurer_account_number']
        firm_provision.shiper_registration_book_number = body['shiper_registration_book_number']

        firm_provision.firm_id = g.firm_id
        firm_provision.client_id = g.client_id
        firm_provision.save_db()

    def update(self, firm_provision: FirmProvision, body: dict):
        firm_provision.title = body['title']
        firm_provision.email_address = body['email_address']
        firm_provision.activity_address = body['activity_address']
        firm_provision.legal_address = body['legal_address']
        firm_provision.phone_number = body['phone_number']

        firm_provision.hvhh = body['hvhh']
        firm_provision.chapter_registration_number = body['chapter_registration_number']
        firm_provision.tax_area_code = body['tax_area_code']
        firm_provision.insurer_account_number = body['insurer_account_number']
        firm_provision.shiper_registration_book_number = body['shiper_registration_book_number']
        firm_provision.save_db()

    def delete(self, firm_provision: FirmProvision):
        firm_provision.delete_db()

    def get_by_id(self, firm_provision_id: int) -> FirmProvision:
        firm_provision: FirmProvision = FirmProvision.query.filter_by(id=firm_provision_id, firm_id=g.firm_id, client_id=g.client_id).first()
        return firm_provision

    def get_all(self, page: int, per_page: int):
        firm_provisions = FirmProvision.query.filter_by(firm_id=g.firm_id, client_id=g.client_id).paginate(page=page, per_page=per_page)
        return self.get_page_items(firm_provisions)
