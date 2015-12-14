from characters import monster

class RockMonster(monster.Monster):

    name = 'Rock Monster'

    def __init__(self):
        super().__init__()

        self.hp = self.hp * 10
        self.mp = self.mp * 0
