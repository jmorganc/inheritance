from abc import ABCMeta, abstractmethod
from weapons import weapon

class MeleeWeapon(weapon.Weapon):

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.name = 'Melee Weapon'
        self.melee = True

        self.mdmg = 0
        self.rdmg = 0
        self.cooldown = 2.5
