import requests


class StationNotFoundError(Exception):
    pass


class OcpAPIClient:
    url_stations = 'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations'
    url_departures = 'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/departures'
    auth_headers = {'Ocp-Apim-Subscription-Key': '9501613007cd41398976a63b0a5bd925'}
    den_haag_centraal_name = 'Den Haag Centraal'
    den_haag_centraal_code = 'GVC'
    train_categories = {'SPR': 'Sprinter', 'IC': 'Intercity'}

    def get_all_stations(self):
        resp_json = requests.get(self.url_stations, headers=self.auth_headers).json()
        stations = [{
            'name': station.get('namen').get('lang'),
            'code': station.get('code')}
            for station in resp_json.get('payload')]
        return stations

    def get_station_code(self, station_name=None):
        # Default to 'Den Haag Centraal'
        station_name = station_name or self.den_haag_centraal_name
        all_stations = self.get_all_stations()
        result_list = [station for station in all_stations if station.get('name') == station_name]
        if len(result_list) < 1:
            raise StationNotFoundError('Station not found')
        else:
            return result_list[0].get('code')

    def get_departures(self, station_code=None):
        # Default to 'Den Haag Centraal'
        station_code = station_code or self.den_haag_centraal_code
        resp_json = requests.get(
            self.url_departures, params={'station': station_code}, headers=self.auth_headers).json()
        if 'payload' not in resp_json:
            raise StationNotFoundError
        departures = resp_json.get('payload').get('departures')
        result = []
        for departure in departures:
            result.append({
                'planned_departure_time': departure.get('plannedDateTime'),
                'direction': departure.get('direction'),
                'platform': departure.get('plannedTrack'),
                'train_type': self.train_categories.get(departure.get('trainCategory')),
            })
        return result