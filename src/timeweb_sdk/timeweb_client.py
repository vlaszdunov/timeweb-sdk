from httpx import Client
from utils.base_client import BaseClient

from .utils import BearerAuth
from .utils.exceptions import *
from .managers import CloudServerManager
import jwt


class TimewebCloudClient:
    """
    Args:
        access_token (str): access token

    Attributes:
        cloud_server_manager (CloudServerManager): Cloud server manager
    """

    def __init__(self, access_token: str) -> None:
        self.__client = BaseClient(access_token)
        self.cloud_server_manager = CloudServerManager(client=self.__client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__client.close_client()
