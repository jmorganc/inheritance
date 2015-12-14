from abc import ABCMeta, abstractmethod
from weapons import weapon

class MeleeWeapon(weapon.Weapon):

    name = 'Melee Weapon'
    melee = True

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.mdmg = 0
        self.rdmg = 0
        self.cooldown = 2.5
