class Room:
    def __init__(self, name, playlist, guest_list, till, entry_fee):
        self.name = name
        self.playlist = []
        self.guest_list = []
        self.till = till
        self.entry_fee = entry_fee

    def check_playlist(self):
        return len(self.playlist)

    def add_new_song(self, song):
        self.playlist.append(song)
    
    def check_in(self, guest):
        self.guest_list.append(guest)
    
    def check_guest_list(self):
        return len(self.guest_list)
    
    def check_out(self, guest):
        self.guest_list.remove(guest)
    
    def check_in_group(self, group):
        self.guest_list.extend(group)

    def availability(self):
        if self.check_guest_list() >= 3:
            return "Sold Out"
        return "Good to go"
    
    def paid_by_guest(self, fee):
        self.till += self.entry_fee



