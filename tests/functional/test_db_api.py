import json
# test create post route
def test_valid_create_post(set_g_user ,test_client, init_database):
    #valid request
    response = test_client.post('/db/post?user_id=1&title=test&content=testcontent&tag=random')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == {"message" :"Post created", "post_id": 13}

    #test with jwt token
    #check it was saved to the db
    response = test_client.get('/db/post?post_id=13')
    assert response.status_code == 200
    response_obj = json.loads(response.data)

    #created is dynamic so test it exists
    assert response_obj['created'] != None
    del response_obj['created'] # unable to compare as it will be made dynmaically
    assert response_obj == {"content" : "testcontent", "flagged": 0, "popularity": 0, "post_id": 13, "tag": "random", "title": "test", "user_id": 1}

def test_invalid_create_post(test_client, init_database):
    #invalid request - missing params
    response = test_client.post('/db/post?user_id=1&title=test')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj  == {"message": "Create post failed"}
    #test without jwt token

# test get post by id route
def test_valid_get_post(test_client, init_database):
    response = test_client.get('/db/post?post_id=1')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == { "content": "Donald trump nukes brazil",  "created": "Sun, 17 May 2020 00:00:00 GMT",  "flagged": 0,  "popularity": 0,  "post_id": 1,  "tag": "party",  "title": "Faker 123",  "user_id": 1}

def test_invalid_get_post(test_client, init_database):
    response = test_client.get('/db/post?post_id=-1')
    assert response.status_code == 500
    response_obj = json.loads(response.data)
    assert response_obj == {"message": "Retrieve post failed"}

#test post update route by id
def test_valid_update_post(test_client, init_database):
    #update post
    response = test_client.put('db/post?post_id=1&title=new&content=new&tag=new')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == {"message" : "Post updated", 'post_id': '1'}
    #check update is saved to db
    response = test_client.get('/db/post?post_id=1')
    assert response.status_code == 200
    response_obj = json.loads(response.data)
    assert response_obj == { "content": "new",  "created": "Sun, 17 May 2020 00:00:00 GMT",  "flagged": 0,  "popularity": 0,  "post_id": 1,  "tag": "new",  "title": "new",  "user_id": 1}

def test_invalid_id_update_post_by_id(test_client, init_database):
    #invalid id
    response = test_client.put('db/post?post_id=-1&title=new&content=new&tag=new')
    assert response.status_code == 400
    response_obj = json.loads(response.data)
    assert response_obj == {"message" : "Post update failed"}

    #missing parameter
    response = test_client.put('db/post?post_id=1&title=new&content=new')
    assert response.status_code == 400
    response_obj = json.loads(response.data)
    assert response_obj == {"message" : "Post update failed"}

#test delete post by id route
def test_valid_delete_post(set_g_user,test_client, init_database):
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

def test_invalid_delete_post(test_client, init_database):
    response = test_client.delete('/db/post?post_id=-1')
    assert response.status_code == 500
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

#test getting mutiple posts routes
def test_get_posts(test_client, init_database):
    #filter by popular
    response = test_client.get('/db/posts')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 10
    assert response_array[0]['popularity'] > response_array[1]['popularity']

    #filter by unpopular
    response = test_client.get('/db/posts?filter=unpop')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 10
    assert response_array[0]['popularity'] < response_array[1]['popularity']

    #filter by newest
    response = test_client.get('/db/posts?filter=new')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 10
    #check dates are in descending order
    assert response_array[0]['created'] == 'Mon, 17 May 2021 00:00:00 GMT'
    assert response_array[1]['created'] == 'Sun, 17 May 2020 00:00:00 GMT'

    #filter by newest
    response = test_client.get('/db/posts?filter=old')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 10
    #check dates are in ascending order
    assert response_array[0]['created'] == 'Mon, 17 May 2010 00:00:00 GMT'
    assert response_array[1]['created'] == 'Thu, 17 May 2012 00:00:00 GMT'

def test_valid_get_user_posts(test_client, init_database):
    #filter by popular
    response = test_client.get('/db/posts?user_id=2')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 6
    assert response_array[0]['popularity'] > response_array[1]['popularity']

    #filter by unpopular
    response = test_client.get('/db/posts?filter=unpop&user_id=2')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 6
    assert response_array[0]['popularity'] < response_array[1]['popularity']

    #filter by newest
    response = test_client.get('/db/posts?filter=new&user_id=2')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 6
    #check dates are in descending order
    assert response_array[0]['created'] == 'Sun, 17 May 2020 00:00:00 GMT'
    assert response_array[1]['created'] == 'Fri, 17 May 2019 00:00:00 GMT'

    #filter by newest
    response = test_client.get('/db/posts?filter=old&user_id=2')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 6
    #check dates are in ascending order
    assert response_array[0]['created'] == 'Sun, 17 May 2015 00:00:00 GMT'
    assert response_array[1]['created'] == 'Tue, 17 May 2016 00:00:00 GMT'

def test_invalid_get_user_posts(test_client, init_database):
    #invalid user_id
    response = test_client.get('/db/posts?user_id=-1')
    assert response.status_code == 400
    response_obj = json.loads(response.data)
    assert response_obj == {"message" : "No posts found"}

def test_valid_get_tag_posts(test_client, init_database):
    #filter by popular
    response = test_client.get('/db/posts?tag=sport')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 2
    assert response_array[0]['popularity'] > response_array[1]['popularity']

    #filter by unpopular
    response = test_client.get('/db/posts?filter=unpop&tag=sport')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 2
    assert response_array[0]['popularity'] < response_array[1]['popularity']

    #filter by newest
    response = test_client.get('/db/posts?filter=new&tag=sport')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 2

    #check dates are in descending order
    assert response_array[0]['created'] == 'Mon, 17 May 2021 00:00:00 GMT'
    assert response_array[1]['created'] == 'Mon, 17 May 2010 00:00:00 GMT'

    #filter by newest
    response = test_client.get('/db/posts?filter=old&tag=sport')
    assert response.status_code == 200
    response_array = json.loads(response.data)
    assert len(response_array) == 2

    #check dates are in ascending order
    assert response_array[0]['created'] == 'Mon, 17 May 2010 00:00:00 GMT'
    assert response_array[1]['created'] == 'Mon, 17 May 2021 00:00:00 GMT'

def test_valid_get_tag_posts(test_client, init_database):
    #invalid tag
    response = test_client.get('/db/posts?tag=abc123')
    assert response.status_code == 400
    response_obj = json.loads(response.data)
    assert response_obj == {"message" : "No posts found"}
