from app.models import Post

def test_post():

    post = Post(title="testing")
    assert post.__repr__() == "<Post 'testing'>"