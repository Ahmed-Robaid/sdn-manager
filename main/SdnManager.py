from sdk.softfire.main import start_manager
from sdk.softfire.manager import AbstractManager


class SdnManager(AbstractManager):
    def release_resources(self, user_info, payload=None) -> None:
        super().release_resources(user_info, payload)

    def list_resources(self, user_info=None, payload=None) -> list:
        return super().list_resources(user_info, payload)

    def validate_resources(self, user_info=None, payload=None) -> None:
        raise KeyError("Not Implemented")

    def provide_resources(self, user_info, payload=None) -> list:
        return super().provide_resources(user_info, payload)

    def create_user(self, username, password):
        super().create_user(username, password)

    def refresh_resources(self, user_info) -> list:
        return super().refresh_resources(user_info)

    def __init__(self, config_file=None) -> None:
        super().__init__()
        self.config_file = config_file


def startManager():
    start_manager(SdnManager(),"etc/sdn-manager.ini")
