# """This will test the music CSV upload"""
# import os
#
# root = os.path.dirname(os.path.abspath(__file__))
# csvdir = os.path.join(root, '../app/uploads')
#
# def test_request_songs(client):
#     """This tests the song page"""
#     response = client.get("/songs")
#     assert response.status_code == 200
#     assert b"Browse: Songs" in response.data
#
# def test_songs_upload(application):
#     """This tests that songs are added to the database"""
#     assert os.path.exists(csvdir) is True
#     filepath = os.path.join(root, '../app/uploads/music.csv')
#     assert os.path.exists(filepath) is True
