from src.UserRoleFirm.IUserRoleFirmRepo import IUserRoleFirmRepo
from .UserRoleFirmModel import UserRoleFirm


class UserRoleFirmRepository(IUserRoleFirmRepo):
    def create(self, user_id: int, role_id: int, firm_id: int or None):
        user_role_firm: UserRoleFirm = UserRoleFirm()
        user_role_firm.role_id = role_id
        user_role_firm.user_id = user_id
        user_role_firm.firm_id = firm_id
        user_role_firm.save_db()

    def get_all(self, user_id: int or None, role_id: int or None, firm_id: int or None):
        user_role_firm: list[UserRoleFirm] = UserRoleFirm.query.filter(
            UserRoleFirm.user_id == user_id if user_id else UserRoleFirm.id.isnot(None),
            UserRoleFirm.role_id == role_id if role_id else UserRoleFirm.id.isnot(None),
            UserRoleFirm.firm_id == firm_id if firm_id else UserRoleFirm.id.isnot(None)
        ).all()
        return user_role_firm

    def get_by_id(self, user_role_firm_id: int, user_id: int or None):
        user_role_firm = UserRoleFirm.query.filter(UserRoleFirm.id == user_role_firm_id,
                                                   UserRoleFirm.user_id == user_id if user_id else UserRoleFirm.id.isnot(None)).first()
        return user_role_firm

    def delete_all_by_user_id(self, user_id: int):
        UserRoleFirm.query.filter_by(user_id=user_id).delete()

    def delete_all_by_firm_id(self, firm_id: int):
        UserRoleFirm.query.filter_by(firm_id=firm_id).delete()
