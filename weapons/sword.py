from weapons import meleeWeapon

class Sword(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 5
