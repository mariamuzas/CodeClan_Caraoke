import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Pepe", 50, 100)

    def test_guest_name(self):
        self.assertEqual("Pepe", self.guest1.name)
    
    def test_guest_wallet(self):
        self.assertEqual(100, self.guest1.wallet)
    
    
    

        
