import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):
   def test_song_name(self):
        self.song_1 = Song("Under Pressure", "Queen")
        self.assertEqual("Under Pressure", self.song_1.title)