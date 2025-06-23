import pytest
from app import app, db

@pytest.fixture
def client():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_user_crud(client):
    # Create
    r = client.post('/users', json={"name": "Bob"})
    assert r.status_code == 201
    user_id = r.json["id"]

    # Get
    r = client.get(f'/users/{user_id}')
    assert r.status_code == 200

    # Delete
    r = client.delete(f'/users/{user_id}')
    assert r.status_code == 200

    # Confirm deletion
    r = client.get(f'/users/{user_id}')
    assert r.status_code == 404
