from weapons import meleeWeapon

class Unarmed(meleeWeapon.MeleeWeapon):

    def __init__(self):
        super().__init__()

        self.name = 'Unamred'
        self.ddmg = 1
        self.cooldown = 5
