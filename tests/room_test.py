import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Supercube", 0, 0)
        self.song_1 = Song("Under Pressure", "Queen")
        self.song_2 = Song("Three Little Birds", "Bob Marley")
        self.song_3 = Song("Eye of the Tiger", "Survivor")
        self.room.playlist = [self.song_1, self.song_2, self.song_3]


    def test_room_name(self):
        self.assertEqual("Supercube", self.room.name)
    
    def test_room_playlist(self):
        self.assertEqual(3, self.room.check_playlist())

    def test_add_new_song(self):
        self.song_4 = Song("My Shot", "Lil-Manuel Miranda")
        self.room.add_new_song_list(self.song_4)
        self.assertEqual(4, self.room.check_playlist())

    
