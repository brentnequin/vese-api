import pytest

from app.api.resources import PostListResource
from app.models import Post
from app import db

@pytest.fixture()
def post_entry(app):

    post = Post(title="test")

    with app.app_context():
        
        db.session.add(Post(title="test"))
        db.session.commit()

    yield post

    # Post.query.filter_by(id=post.id).delete()
    
def test_post_list_resource(app, post_entry):

    with app.app_context():
        post_list_resource = PostListResource()
        post = post_list_resource.get()[0]

    assert post['title'] == 'test'