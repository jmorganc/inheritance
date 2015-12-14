from weapons import meleeWeapon

class Wand(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 0
        self.mdmg = 10
