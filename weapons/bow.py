from weapons import rangedWeapon

class Bow(rangedWeapon.RangedWeapon):

    def __init__(self):
        super().__init__()

        self.name = 'Bow'
        self.rdmg = 7.5
