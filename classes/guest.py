class Guest:
    def __init__(self, name, age, wallet,fave_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fave_song = fave_song
    
    def pay_for_room(self, fee):
        self.wallet -= fee

    