from app.views import hello_world

def test_route_index():

    assert hello_world() == "<p>Hello, World!</p>"