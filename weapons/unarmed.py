from weapons import meleeWeapon

class Unarmed(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 1
