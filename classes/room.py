class Room:
    def __init__(self, name, playlist, guest_list):
        self.name = name
        self.playlist = []
        self.guest_list = []

    def check_playlist(self):
        return len(self.playlist)

    def add_new_song(self, song):
        self.playlist.append(song)
    
    def check_in(self, customer):
        self.guest_list.append(customer)
    
    def check_guest_list(self):
        return len(self.guest_list)
    
    def check_out(self, customer):
        self.guest_list.remove(customer)

