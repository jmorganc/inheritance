from weapons import meleeWeapon

class Sword(meleeWeapon.MeleeWeapon):

    name = 'Sword'

    def __init__(self):
        super().__init__()

        self.ddmg = 5
        self.cooldown = 5
