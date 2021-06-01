from backend import settings

def test_integration_residencias(client):

    response = client.get('/v1/api/wipro/residencias', params={}, status='*')
    assert response.status_code == 200

def test_integration_preco_medio(client):

    response = client.get('/v1/api/wipro/preco-medio', params={}, status='*')
    assert response.status_code == 200