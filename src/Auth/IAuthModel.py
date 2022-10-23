from abc import ABC, abstractmethod
from src.__Parents.Service import Service
from .AuthModel import Auth


class IAuthModel(ABC):
    @abstractmethod
    def generate_tokens(self, user_id: int):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int):
        pass

    @abstractmethod
    def update_setting(self, auth_id: int or None, body: dict, user_id: int or None):
        pass

