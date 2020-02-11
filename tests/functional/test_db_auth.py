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
