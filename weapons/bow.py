from weapons import rangedWeapon

class Bow(rangedWeapon.RangedWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 0
        self.rdmg = 7.5
