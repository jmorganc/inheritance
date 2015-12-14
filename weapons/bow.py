from weapons import rangedWeapon

class Bow(rangedWeapon.RangedWeapon):

    name = 'Bow'

    def __init__(self):
        super().__init__()

        self.rdmg = 7.5
