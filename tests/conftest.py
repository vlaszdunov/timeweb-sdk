import pytest
import respx
import json
from pathlib import Path

from respx import MockRouter

TEST_DATA_DIR = Path("tests/test_data")


def load_correct_data(folder_name: str):
    test_data = TEST_DATA_DIR / folder_name / "correct.json"
    return json.load(test_data.open(encoding="utf-8"))


def load_response_data(folder_name: str):
    test_data = TEST_DATA_DIR / folder_name / "response.json"
    return json.load(test_data.open(encoding="utf-8"))


def check_request_headers(request: MockRouter):
    assert request.calls[0].request.headers["Authorization"] == "Bearer <API_TOKEN>"
    assert request.calls[0].request.headers["Content-Type"] == "application/json"


@pytest.fixture(scope="session")
def timeweb_mocked_api():
    with respx.mock(base_url="https://api.timeweb.cloud/api/v1", assert_all_called=False) as respx_mock:
        yield respx_mock
