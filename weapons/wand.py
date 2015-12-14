from weapons import magicWeapon

class Wand(magicWeapon.MagicWeapon):

    def __init__(self):
        super().__init__()

        self.dmg = 2
        self.mdmg = 10
