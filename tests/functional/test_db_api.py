import json
# test create post route
def test_valid_create_post(test_client, init_database):
    #valid request
    response = test_client.post('/db/post?user_id=1&title=test&content=testcontent&tag=random')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == {"message" :"Post created", "post_id": 2}

    #test with jwt token
    #check it was saved to the db
    response = test_client.get('/db/post?post_id=2')
    assert response.status_code == 200
    response_obj = json.loads(response.data)

    #created is dynamic so test it exists
    assert response_obj['created'] != None
    del response_obj['created'] # unable to compare as it will be made dynmaically
    assert response_obj == {"content" : "testcontent", "flagged": 0, "popularity": 0, "post_id": 2, "tag": "random", "title": "test", "user_id": 1}

def test_invalid_create_post(test_client, init_database):
    #invalid request - missing params
    response = test_client.post('/db/post?user_id=1&title=test')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj  == {"message": "Create post failed"}
    #test without jwt token

# test get post by id route
def test_valid_get_post_by_id(test_client, init_database):
    response = test_client.get('/db/post?post_id=1')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == { "content": "Donald trump nukes brazil",  "created": "Sun, 17 May 2020 00:00:00 GMT",  "flagged": 0,  "popularity": 0,  "post_id": 1,  "tag": "party",  "title": "Faker 123",  "user_id": 1}

def test_invalid_get_post_by_id(test_client, init_database):
    response = test_client.get('/db/post?post_id=-1')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "Retrieve post failed"}

#test delete post by id route
def test_valid_delete_post_by_id(test_client, init_database):
    #delete post 
    response = test_client.delete('/db/post?post_id=1')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "Post deleted"}

    #check db for post
    response = test_client.get('/db/post?post_id=1')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "Retrieve post failed"}

def test_invalid_delete_post_by_id(test_client, init_database):
    response = test_client.delete('/db/post?post_id=-1')
    assert response.status_code == 400
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "Delete post failed"}

# test access user data route
def test_valid_get_user(test_client, init_database):
    response = test_client.get('/db/user?user_id=1')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    response_obj = {
            "user_id": 1,
            "username": "test",
            "moderator": False,
            "private": False,
        }

def test_invalid_get_user(test_client, init_database):
    response = test_client.get('/db/user?user_id=-1')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "request failed"}

