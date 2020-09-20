import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Supercube", 0, 0, 50, 10)
        self.song_1 = Song("Under Pressure", "Queen")
        self.song_2 = Song("Three Little Birds", "Bob Marley")
        self.song_3 = Song("Eye of the Tiger", "Survivor")
        self.room.playlist = [self.song_1, self.song_2, self.song_3]
        self.guest1 = Guest("Pepe", 50, 100)
        self.room.guest_list = [self.guest1]

    def test_room_name(self):
        self.assertEqual("Supercube", self.room.name)
    
    def test_room_playlist(self):
        self.assertEqual(3, self.room.check_playlist())
    
    def test_till(self):
        self.assertEqual(50, self.room.till)

    def test_add_new_song(self):
        self.song_4 = Song("My Shot", "Lil-Manuel Miranda")
        self.room.add_new_song(self.song_4)
        self.assertEqual(4, self.room.check_playlist())

    def test_check_in_guest(self):
        self.guest2 = Guest("Lola", 42, 200)
        self.room.check_in(self.guest2)
        self.assertEqual(2, self.room.check_guest_list())
    
    def test_check_out_guesst(self):
        self.room.check_out(self.guest1)
        self.assertEqual(0, self.room.check_guest_list())

    def test_check_in_sold_out(self):
        self.guest2 = Guest("Lola", 42, 200)
        self.guest3 = Guest("Manoli", 53, 50)
        self.guest4 = Guest("Jose Mari", 45, 100)
        self.guest_group = [self.guest2, self.guest3, self.guest4]
        self.room.check_in_group(self.guest_group)
        self.assertEqual("Sold Out", self.room.availability())
    
    def test_room_take_fee_paid_by_guest(self):
        self.guest1.pay_for_room(self.room.entry_fee)
        self.room.paid_by_guest(self.room.entry_fee)
        self.assertEqual(60, self.room.till)


    
