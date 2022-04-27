"""This tests that music.csv is uploaded"""

import os

def song_upload_test(client):
   """Testing song uploads"""
   response = client.get('/uploads/music.csv')
   assert response.status_code == 200
   assert os.path.isfile('music.csv')
