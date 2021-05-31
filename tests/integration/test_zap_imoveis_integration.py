from backend import settings

def test_vivareal_integration(client, main_url_zap_imoveis):

    response = client.get(main_url_zap_imoveis, params={}, status='*')

    assert response.status_code == 200

    res = response.json[0]
    assert res.get('pageNumber') == settings.STANDARD_PAGE_NUMBER
    assert res.get('pageSize') == settings.STANDARD_PER_PAGE
    assert res.get('totalCount') == 917
    assert len(res.get('listings')) == 10

def test_vivareal_integration_with_page_number(client, main_url_zap_imoveis):

    params = {
        "pageNumber": 52
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')

    assert response.status_code == 200

    res = response.json[0]
    assert res.get('pageNumber') == 52
    assert res.get('pageSize') == settings.STANDARD_PER_PAGE
    assert res.get('totalCount') == 917
    assert len(res.get('listings')) == 10

def test_vivareal_integration_with_per_page(client, main_url_zap_imoveis):

    params = {
        "perPage": 75
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')

    assert response.status_code == 200

    res = response.json[0]
    assert res.get('pageNumber') == settings.STANDARD_PAGE_NUMBER
    assert res.get('pageSize') == 75
    assert res.get('totalCount') == 917
    assert len(res.get('listings')) == 75

def test_vivareal_integration_with_per_page_and_page_number(client, main_url_zap_imoveis):

    params = {
        "pageNumber": 3,
        "perPage": 33
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')

    assert response.status_code == 200

    res = response.json[0]
    assert res.get('pageNumber') == 3
    assert res.get('pageSize') == 33
    assert res.get('totalCount') == 917
    assert len(res.get('listings')) == 33