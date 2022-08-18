from app.api.schemas import PostSchema

def test_post_schema():

    post_schema = PostSchema()
    assert post_schema.__repr__() == "<PostSchema(many=False)>"