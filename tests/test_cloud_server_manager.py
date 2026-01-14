import pytest
from httpx import Response
import re

from timeweb_sdk.managers import CloudServerManager
from conftest import load_response_data, load_correct_data, check_request_headers

TEST_API_TOKEN = "<API_TOKEN>"
server_manager = CloudServerManager(TEST_API_TOKEN)

list_of_servers_response = load_response_data("cloud_servers/get_all_servers")
server_response = load_response_data("cloud_servers/get_server_by_id")
os_list_response = load_response_data("cloud_servers/get_os")
presets_list_response = load_response_data("cloud_servers/get_server_presets")
server_configs_response = load_response_data("cloud_servers/get_server_configs")
available_software_response = load_response_data("cloud_servers/get_available_software")

list_of_servers_correct = load_correct_data("cloud_servers/get_all_servers")
server_correct = load_correct_data("cloud_servers/get_server_by_id")
os_list_correct = load_correct_data("cloud_servers/get_os")
presets_list_correct = load_correct_data("cloud_servers/get_server_presets")
server_configs_correct = load_correct_data("cloud_servers/get_server_configs")
available_software_correct = load_correct_data("cloud_servers/get_available_software")


@pytest.fixture(scope="module")
def cloud_servers_mock_api(timeweb_mocked_api):
    server_list_route = timeweb_mocked_api.get("/servers", name="get_list_of_servers")
    server_list_route.return_value = Response(200, json=list_of_servers_response)

    server_by_id_route = timeweb_mocked_api.get(re.compile(r"/servers/\d+"), name="get_server_by_id")
    server_by_id_route.return_value = Response(200, json=server_response)

    os_list_route = timeweb_mocked_api.get("/os/servers", name="get_os")
    os_list_route.return_value = Response(200, json=os_list_response)

    presets_list_route = timeweb_mocked_api.get("/presets/servers", name="get_server_presets")
    presets_list_route.return_value = Response(200, json=presets_list_response)

    config_list_route = timeweb_mocked_api.get("/configurator/servers", name="get_server_configs")
    config_list_route.return_value = Response(200, json=server_configs_response)

    available_software_route = timeweb_mocked_api.get("/software/servers", name="get_available_software")
    available_software_route.return_value = Response(200, json=available_software_response)

    return timeweb_mocked_api


def test_get_all_servers(cloud_servers_mock_api):
    response = server_manager.get_all_servers()

    response[0] = response[0].__dict__
    response[0]["drives"][0] = response[0]["drives"][0].__dict__
    response[0]["software"] = response[0]["software"].__dict__
    response[0]["networks"][0] = response[0]["networks"][0].__dict__
    response[0]["networks"][0]["ips"][0] = response[0]["networks"][0]["ips"][0].__dict__
    response[0]["os"] = response[0]["os"].__dict__

    assert cloud_servers_mock_api["get_list_of_servers"].called
    check_request_headers(cloud_servers_mock_api["get_list_of_servers"])
    assert len(response) == len(list_of_servers_correct["servers"])
    assert response == list_of_servers_correct["servers"]


def test_server_by_id(cloud_servers_mock_api):
    response = server_manager.get_server_by_id(1)

    response = response.__dict__
    response["drives"][0] = response["drives"][0].__dict__
    response["software"] = response["software"].__dict__
    response["networks"][0] = response["networks"][0].__dict__
    response["networks"][0]["ips"][0] = response["networks"][0]["ips"][0].__dict__
    response["os"] = response["os"].__dict__

    assert cloud_servers_mock_api["get_server_by_id"].called
    assert response == server_correct["server"]


def test_get_os(cloud_servers_mock_api):
    response = server_manager.get_os()

    response[0] = response[0].__dict__
    response[0]["requirements"] = response[0]["requirements"].__dict__

    assert cloud_servers_mock_api["get_os"].called
    assert response == os_list_correct["servers_os"]


def test_get_server_presets(cloud_servers_mock_api):
    response = server_manager.get_server_presets()
    for i in range(len(response)):
        response[i] = response[i].__dict__

    assert cloud_servers_mock_api["get_server_presets"].called
    assert response == presets_list_correct["server_presets"]


def test_get_server_configs(cloud_servers_mock_api):
    response = server_manager.get_server_configs()
    for i in range(len(response)):
        response[i] = response[i].__dict__
        response[i]["requirements"] = response[i]["requirements"].__dict__

    assert cloud_servers_mock_api["get_server_configs"].called
    assert response == server_configs_correct["server_configurators"]


def test_get_available_software(cloud_servers_mock_api):
    pass
