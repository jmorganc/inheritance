from weapons import weapon

class MeleeWeapon(weapon.Weapon):

    def __init__(self):
        super().__init__()

        self.dmg = 5
