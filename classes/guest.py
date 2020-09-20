class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
    
    def pay_for_room(self, fee):
        self.wallet -= fee