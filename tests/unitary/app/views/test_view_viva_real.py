def test_view_viva_real_success(client, main_url_viva_real):
    response = client.get(main_url_viva_real, params={}, status='*')
    assert response.status_code == 200

def test_view_viva_real_success_with_params(client, main_url_viva_real):
    params = {
        "pageNumber": 3,
        "perPage": 15
    }
    response = client.get(main_url_viva_real, params=params, status='*')
    assert response.status_code == 200

def test_view_viva_real_page_number_error(client, main_url_viva_real):

    params = {
        "pageNumber": "string",
    }
    response = client.get(main_url_viva_real, params=params, status='*')
    assert response.status_code == 400
    assert response.json == {
        'message': {
            'pageNumber': ['Invalid PageNumber.']
        }
    }

def test_view_viva_real_per_page_error(client, main_url_viva_real):

    params = {
        "perPage": "string",
    }
    response = client.get(main_url_viva_real, params=params, status='*')
    assert response.status_code == 400
    assert response.json == {
        'message': {
            'perPage': ['Not a valid integer.']
        }
    }