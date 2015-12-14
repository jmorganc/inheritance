from weapons import meleeWeapon

class Unarmed(meleeWeapon.MeleeWeapon):

    name = 'Unarmed'

    def __init__(self):
        super().__init__()

        self.ddmg = 1
        self.cooldown = 5
