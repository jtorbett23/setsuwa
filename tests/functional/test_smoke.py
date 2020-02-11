#test '/' route to check pytest is working properly

def test_app_running_route(test_client):
    response = test_client.get('/running')
    assert response.status_code == 200
    assert b"app is running" in response.data

