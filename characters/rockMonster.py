from characters import monster

class RockMonster(monster.Monster):

    def __init__(self, name='Rock Monster'):
        self.name = name
        super().__init__()

        self.hp_max = self.hp_max * 10
        self.hp = self.hp * 10
        self.mp_max = self.mp_max * 10
        self.mp = self.mp * 0
