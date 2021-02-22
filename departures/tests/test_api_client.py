import json
import pytest
from unittest.mock import patch

from departures.api_client.ocp_api_client_v2 import OcpAPIClient, StationNotFoundError


@pytest.fixture
def response_all_stations():
    def get_json():
        with open('departures/tests/src_all_stations.json', 'r') as f:
            json_response_all_stations = f.read()
            return json.loads(json_response_all_stations)
    return get_json


@pytest.fixture
def response_departures():
    def get_json():
        with open('departures/tests/src_departures.json', 'r') as f:
            json_response_departures = f.read()
            return json.loads(json_response_departures)
    return get_json


@patch('requests.get')
def test_all_stations(mock_get, response_all_stations):
    mock_get.return_value.json = response_all_stations
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    with open('departures/tests/expected_stations.json', 'r') as f:
        expected_all_stations = json.loads(f.read())
    assert all_stations == expected_all_stations


@patch('requests.get')
def test_get_station_code(mock_get, response_all_stations):
    mock_get.return_value.json = response_all_stations
    client = OcpAPIClient()
    station_code = client.get_station_code()
    assert station_code == 'GVC'


@patch('requests.get')
def test_get_station_code_raises(mock_get, response_all_stations):
    mock_get.return_value.json = response_all_stations
    client = OcpAPIClient()
    with pytest.raises(StationNotFoundError):
        station_code = client.get_station_code('Wrong name')


@patch('requests.get')
def test_get_departures(mock_get, response_departures):
    mock_get.return_value.json = response_departures
    client = OcpAPIClient()
    departures = client.get_departures()
    with open('departures/tests/expected_departures.json', 'r') as f:
        expected_departures = json.loads(f.read())
    assert departures == expected_departures