from fastapi.testclient import TestClient

from main import apps

client = TestClient(apps)



# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}
#
#
def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
# def test_create_user():
#     response = client.post("/api/users", headers={"X-token": "coneofsilence"},
#                            json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},)
#     assert response.status_code == 200

