import logging

from app import db
from app.db.models import User, Song


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
        user.songs = [Song("test", "smap", "dsf", "sdf"), Song("test2", "te", "dsf", "sdf")]
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
