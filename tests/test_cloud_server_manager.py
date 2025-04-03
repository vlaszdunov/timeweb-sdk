import re
import pytest
import respx
import json
from httpx import Response
from timeweb_sdk.managers import CloudServerManager
from timeweb_sdk.entities import CloudServer
from pathlib import Path
TEST_API_TOKEN = "<API_TOKEN>"

list_of_servers_response=json.load(Path("./test_data/get_all_servers_response.json").open(encoding="utf-8"))
list_of_servers=json.load(Path("./test_data/get_all_servers_eq.json").open(encoding="utf-8"))

server_manager = CloudServerManager(TEST_API_TOKEN)

@pytest.fixture
def timeweb_mocked_api():
    with respx.mock(base_url="https://api.timeweb.cloud/api/v1", assert_all_called=False) as respx_mock:
        server_list_route = respx_mock.get("/servers", name="get_list_of_servers")
        server_list_route.return_value = Response(200, json=list_of_servers_response)

        yield respx_mock


def test_get_all_servers(timeweb_mocked_api):

    response = server_manager.get_list_of_servers()
    expected_servers = [CloudServer(TEST_API_TOKEN, **server) for server in list_of_servers_response["servers"]]

    response_servers = []
    for server in response:
        server_dict = server.__dict__.copy()

        # Convert any nested objects to dicts if needed
        for key, value in server_dict.items():
            if hasattr(value, '__dict__'):
                server_dict[key] = value.__dict__
            elif isinstance(value, list):
                for item in value:
                    if hasattr(item, '__dict__'):
                        server_dict[key] = item.__dict__
        response_servers.append(server_dict)
    #
    print(*response[0].drives)
    assert timeweb_mocked_api["get_list_of_servers"].called
    # assert response_servers == list_of_servers["servers"]
