from characters import player

class WarriorPlayer(player.Player):

    def __init__(self, name='Warrior'):
        super().__init__()

        self.name = name

        self.hp_max = self.hp_max * 10
        self.hp = self.hp * 10
        self.mp_max = self.mp_max * 10
        self.mp = self.mp * 0
