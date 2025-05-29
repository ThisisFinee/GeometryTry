import math

def test_list_shapes(client):
    response = client.get('/shapes')
    assert response.status_code == 200
    data = response.json()
    assert 'circle' in data and data['circle'] == 'Circle'
    assert 'triangle' in data and data['triangle'] == 'Triangle'


def test_compute_area_circle(client):
    payload = {'type': 'circle', 'parameters': {'radius': 2}}
    response = client.post('/compute-area', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['type'] == 'Circle'
    assert math.isclose(data['area'], math.pi * 4)
    assert data['additional']['text'] == "Valid circle"
    assert data['additional']['is_specific'] is False


def test_compute_area_triangle_auto_detect(client):
    payload = {'parameters': {'a': 3, 'b': 4, 'c': 5}}
    response = client.post('/compute-area', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['type'] == 'Triangle'
    assert math.isclose(data['area'], 6.0)
    assert data['additional']['text'] == "It's a right-anled triangle"
    assert data['additional']['is_specific'] is True


def test_invalid_shape_type(client):
    payload = {'type': 'hexagon', 'parameters': {'a': 1}}
    response = client.post('/compute-area', json=payload)
    assert response.status_code == 400
    assert 'Unknown shape type' in response.json()['detail']


def test_invalid_params(client):
    payload = {'type': 'circle', 'parameters': {'radius': -1}}
    response = client.post('/compute-area', json=payload)
    assert response.status_code == 400
    assert 'Invalid parameters' in response.json()['detail']
