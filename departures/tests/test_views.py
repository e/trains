from django.urls import reverse


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context.get('all_stations')) > 0


def test_departures(client):
    url = reverse('departures', kwargs={'station_code':'GVC'})
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context.get('departures')) > 0


def test_departures_raises(client):
    url = reverse('departures', kwargs={'station_code': 'WRONG_CODE'})
    resp = client.get(url)
    assert resp.status_code == 404

