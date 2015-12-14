from abc import ABCMeta, abstractmethod
from weapons import weapon

class RangedWeapon(weapon.Weapon):

    name = 'Ranged Weapon'
    ranged = True

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.ddmg = 0
        self.rdmg = 0
        self.cooldown = 5
