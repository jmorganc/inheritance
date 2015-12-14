from weapons import meleeWeapon

class Sword(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.name = 'Sword'
        self.ddmg = 5
        self.cooldown = 5
