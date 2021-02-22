import requests


class OcpAPIClient:
    url_stations = 'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations'
    url_departures = 'https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/departures'
    auth_headers = {'Ocp-Apim-Subscription-Key': '9501613007cd41398976a63b0a5bd925'}
    den_haag_centraal_name = 'Den Haag Centraal'
    train_categories = {'SPR': 'Sprinter', 'IC': 'Intercity'}

    def get_station_code(self, station_name=None):
        # Default to 'Den Haag Centraal'
        station_name = station_name or self.den_haag_centraal_name
        resp_json = requests.get(self.url_stations, headers=self.auth_headers).json()
        result_list = [station for station in resp_json.get('payload') if station.get(
            'namen').get('lang') == station_name]
        if len(result_list) != 1:
            raise Exception('Station not found')
        else:
            return result_list[0].get('code')

    def get_departures(self, station_name=None):
        station_name = station_name or self.den_haag_centraal_name
        station_code = self.get_station_code(station_name)
        resp = requests.get(self.url_departures, params={'station': station_code}, headers=self.auth_headers)
        departures = resp.json().get('payload').get('departures')
        result = []
        for departure in departures:
            result.append({
                'planned_departure_time': departure.get('plannedDateTime'),
                'direction': departure.get('direction'),
                'platform': departure.get('plannedTrack'),
                'train_type': self.train_categories.get(departure.get('trainCategory')),
            })
        return result