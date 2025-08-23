from httpx import Client
from jwt import InvalidTokenError

from utils import BearerAuth
from utils.exceptions import *
from managers import CloudServerManager
import jwt


class TimewebCloudClient:
    """
    Args:
        access_token (str): access token

    Attributes:
        cloud_server_manager (CloudServerManager): Cloud server manager
    """

    __access_token: str
    __client: Client
    cloud_server_manager: CloudServerManager

    def __init__(self, access_token: str) -> None:
        self.__verify_token(access_token)
        self.__access_token = access_token
        self.__client = Client(
            auth=BearerAuth(self.__access_token),
            base_url="https://access.timeweb.cloud/api/v1",
            headers={"Content-Type": "application/json"},
            http2=True,
        )
        self.cloud_server_manager = CloudServerManager(self.__access_token, client=self.__client)

    def close_client(self):
        self.__client.close()

    def __verify_token(self, access_token: str):
        try:
            jwt.decode(
                access_token,
                options={
                    "verify_signature": False,
                    "verify_exp": True,
                    "verify_nbf": True,
                },
            )
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredAccessTokenError() from None
        except jwt.exceptions.InvalidTokenError or jwt.exceptions.ImmatureSignatureError:
            raise InvalidToken() from None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close_client()
