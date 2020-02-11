# # test create post route
def test_valid_create_post(test_client, init_database):
    #valid request
    response = test_client.post('/db/post?user_id=1&title=test&content=testcontent&tag=random')
    assert response.status_code == 200
    assert b'{\n    "message": "Post created",\n    "post_id": 2\n}\n'  in response.data
    #test with jwt token

def test_invalid_create_post(test_client, init_database):
    #invalid request - missing params
    response = test_client.post('/db/post?user_id=1&title=test')
    assert response.status_code == 500
    assert b'{\n    "message": "Create post failed"\n}\n'  in response.data
    #test without jwt token

# test get post by id route
def test_valid_get_post_by_id(test_client, init_database):
    response = test_client.get('/db/post?post_id=1')
    assert response.status_code == 200
    assert b'{\n  "content": "Donald trump nukes brazil", \n  "created": "Sun, 17 May 2020 00:00:00 GMT", \n  "flagged": 0, \n  "popularity": 0, \n  "post_id": 1, \n  "tag": "party", \n  "title": "Faker 123", \n  "user_id": 1\n}\n' in response.data

def test_invalid_get_post_by_id(test_client, init_database):
    response = test_client.get('/db/post?post_id=-1')
    assert response.status_code == 500
    assert b'{\n    "message": "Retrieve post failed"\n}\n' in response.data

