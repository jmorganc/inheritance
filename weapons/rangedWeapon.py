from abc import ABCMeta, abstractmethod
from weapons import weapon

class RangedWeapon(weapon.Weapon):

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.name = 'Ranged Weapon'
        self.ranged = True

        self.ddmg = 0
        self.rdmg = 0
        self.cooldown = 5
