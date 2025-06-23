import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_and_get_user(client):
    response = client.post('/users', json={"name": "Alice"})
    assert response.status_code == 201
    user_id = response.json["id"]

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json["name"] == "Alice"
