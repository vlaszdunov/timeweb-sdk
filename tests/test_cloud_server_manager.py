import pytest
import respx
import json
from httpx import Response
from timeweb_sdk.managers import CloudServerManager
from pathlib import Path

TEST_API_TOKEN = "<API_TOKEN>"

list_of_servers_response = json.load(Path("tests/test_data/get_all_servers_response.json").open(encoding="utf-8"))
list_of_servers = json.load(Path("tests/test_data/get_all_servers_eq.json").open(encoding="utf-8"))

server_manager = CloudServerManager(TEST_API_TOKEN)


@pytest.fixture
def timeweb_mocked_api():
    with respx.mock(base_url="https://api.timeweb.cloud/api/v1", assert_all_called=False) as respx_mock:
        server_list_route = respx_mock.get("/servers", name="get_list_of_servers")
        server_list_route.return_value = Response(200, json=list_of_servers_response)

        yield respx_mock


def test_get_all_servers(timeweb_mocked_api):
    response = server_manager.get_list_of_servers()

    response[0] = response[0].__dict__
    response[0]["drives"][0] = response[0]["drives"][0].__dict__
    response[0]["software"] = response[0]["software"].__dict__
    response[0]["networks"][0] = response[0]["networks"][0].__dict__
    response[0]["networks"][0]["ips"][0] = response[0]["networks"][0]["ips"][0].__dict__
    response[0]["os"] = response[0]["os"].__dict__

    assert timeweb_mocked_api["get_list_of_servers"].called
    assert len(response) == len(list_of_servers_response["servers"])
    assert response == list_of_servers["servers"]
