class Room:
    def __init__(self, name, playlist, guest_list):
        self.name = name
        self.playlist = []
        self.guest_list = []

    def check_playlist(self):
        return len(self.playlist)

    # def add_new_song_list(self, song):
