from httpx import Auth as __Auth


class BearerAuth(__Auth):
    def __init__(self, access_token: str):
        self.__access_token = access_token

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self.__access_token}"
        yield request
