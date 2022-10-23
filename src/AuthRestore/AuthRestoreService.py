from .IAuthRestoreRepo import IAuthRestoreRepo
from ..__Parents.Service import Service
from ..User.IUserRepo import IUserRepo
from src.__Parents.Email import Email


class AuthRestoreService(Service, Email):
    def __init__(self, auth_restore_repository: IAuthRestoreRepo, user_repository: IUserRepo):
        self.auth_restore_repository: IAuthRestoreRepo = auth_restore_repository
        self.user_repository: IUserRepo = user_repository

    def create(self, body: dict) -> dict:
        user = self.user_repository.get_by_email_address(email_address=body['email_address'])
        if not user:
            return self.response_not_found("по такому эл. адресу пользователь не сушествует")

        auth_restore = self.auth_restore_repository.get(user_id=user.id, ticket=None)
        new_ticket: str = self.generate_ticket_code()
        if not auth_restore:
            self.auth_restore_repository.create(user_id=user.id, ticket=new_ticket)
        else:
            self.auth_restore_repository.update(auth_restore=auth_restore, ticket=new_ticket)

        try:
            self.send_by_email(email_addresses=[user.email_address],
                               message_body=f"ваш код для сбрoса пароля {new_ticket}")
            return self.response_created("проверте ваш электронный адрес")
        except:
            return self.response_not_found("электронный аддресс пользователя верный на этом сайте, "
                                           "но такого электронного адреса не существует на самом деле, "
                                           "по этому код не может быть отправлен ")


    def restore(self, body: dict) -> dict:
        auth_restore = self.auth_restore_repository.get(ticket=body['ticket'], user_id=None)
        if not auth_restore:
            return self.response_not_found("код не верный")

        self.user_repository.update_auth(user_id=auth_restore.user_id, body=body)
        return self.response_updated("обновление данных прошло успешно")
