from weapons import meleeWeapon

class Bow(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 0
        self.rdmg = 7.5
