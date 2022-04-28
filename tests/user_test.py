import logging

from app import db
from app.db.models import User, Song
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        user = User.query.filter_by(email='test@test.com').first()
        log.info(user)
        assert user.email == 'test@test.com'
        user.songs = [Song("test","smap","dsf","sdf"),Song("test2","te","dsf","sdf")]
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        song1.title = "SuperSongTitle"
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0


def test_register(client):
    """This will test the register function"""

    """ POST to /register """
    new_email = 'newuser@test.test'
    new_password = 'Test1234!'
    data = {
        'email': new_email,
        'password': new_password,
        'confirm': new_password
    }
    response = client.post('/register', data=data)
    assert response.status_code == 302

    # verify new user is in database
    new_user = User.query.filter_by(email=new_email).first()
    assert new_user.email == new_email

    db.session.delete(new_user)  # pylint: disable=no-member
