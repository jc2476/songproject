"""New registration test"""
from app import User, db


def test_register(client):
    """This will test the register function"""
    new_email = 'newuser@test.test'
    new_password = 'Test1234!'
    data = {
        'email': new_email,
        'password': new_password,
        'confirm': new_password,
    }
    response = client.post('register', data=data)
    assert response.status_code == 302

    # This is to verify that a new user is in the database
    new_user = User.query.filter_by(email=new_email).first()
    assert new_user.email == new_email

    # verify that function will deny an already registered user
    response2 = client.post('register', data=data)
    assert response2.status_code == 302

    # delete test user from db
    db.session.delete(new_user)  # pylint: disable=no-member
    assert db.session.query(User).count() == 0
