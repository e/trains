from django.http import Http404
from django.shortcuts import render

from departures.api_client.ocp_api_client_v2 import OcpAPIClient
from departures.api_client.ocp_api_client_v2 import StationNotFoundError


def index(request):
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    context = {'all_stations': all_stations}
    return render(request, 'departures/index.html', context)

def departures(request, station_code):
    client = OcpAPIClient()
    try:
        departures = client.get_departures(station_code)
    except StationNotFoundError:
        raise Http404
    context = {'departures': departures, 'station_code': station_code}
    return render(request, 'departures/departures.html', context)
