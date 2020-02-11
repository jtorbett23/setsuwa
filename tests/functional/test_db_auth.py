import json
#test register user
def test_valid_registration(test_client, init_database):
    #valid request
    response = test_client.post('/auth/register?username=new&password=user')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj  == {"message" : "new has been created"}
    #test user is now in database - jwt protected
    response = test_client.get('/db/user?user_id=2')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj  == {
            "user_id": 2,
            "username": "new",
            "moderator": False,
            "private": False,
        }

def test_already_registered(test_client, init_database):
    #user already exists
    response = test_client.post('/auth/register?username=test&password=abc')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj  == {'message': 'User test already exists'}


def test_valid_registration(test_client, init_database):
    #invalid request 
    response = test_client.post('/auth/register?username=new')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj  == {'message': 'Something went wrong'}


#test login
def test_valid_login(test_client, init_database):
    response = test_client.post('/auth/login?username=test&password=pass')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    #dynamic values so test they exist
    assert response_obj['access_token'] != None
    assert response_obj['refresh_token'] != None
    assert response_obj['user_id'] == 1

def test_invalid_login(test_client, init_database):
    #invalid password
    response = test_client.post('/auth/login?username=test&password=pass1')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    #dynamic values so test they exist
    assert response_obj == {'message': 'Incorrect username/password'}

    #invalid password
    response = test_client.post('/auth/login?username=test1&password=pass')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    #dynamic values so test they exist
    assert response_obj == {'message': 'Incorrect username/password'}

#get access and refresh tokens
def get_jwt_tokens(client):
    response = client.post('/auth/login?username=test&password=pass')
    response_obj = json.loads(response.data)
    return response_obj

#logout access token route
def test_valid_logout_access(test_client, init_database):
    jwt_tokens = get_jwt_tokens(test_client)
    auth_header={'Authorization': 'Bearer '+jwt_tokens['access_token']}
    response = test_client.post('/auth/logoutAccess', headers=auth_header)
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == {'message': 'Access token has been revoked'}


def test_invalid_logout_access(test_client, init_database):
    response = test_client.post('/auth/logoutAccess')
    assert response.status_code == 401
    response_obj = json.loads(response.data)
    assert response_obj == {'msg': 'Missing Authorization Header'}

    

