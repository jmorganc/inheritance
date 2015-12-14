from weapons import magicWeapon

class Wand(magicWeapon.MagicWeapon):

    name = 'Wand'

    def __init__(self):
        super().__init__()

        self.ddmg = 2
        self.mdmg = 10
