def test_view_zap_success(client, main_url_zap_imoveis):
    response = client.get(main_url_zap_imoveis, params={}, status='*')
    assert response.status_code == 200

def test_view_zap_success_with_params(client, main_url_zap_imoveis):
    params = {
        "pageNumber": 3,
        "perPage": 15
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')
    assert response.status_code == 200

def test_view_zap_page_number_error(client, main_url_zap_imoveis):

    params = {
        "pageNumber": "string",
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')
    assert response.status_code == 400
    assert response.json == {
        'message': {
            'pageNumber': ['Invalid PageNumber.']
        }
    }

def test_view_zap_per_page_error(client, main_url_zap_imoveis):

    params = {
        "perPage": "string",
    }
    response = client.get(main_url_zap_imoveis, params=params, status='*')
    assert response.status_code == 400
    assert response.json == {
        'message': {
            'perPage': ['Not a valid integer.']
        }
    }