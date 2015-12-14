from abc import ABCMeta, abstractmethod
from weapons import weapon

class MagicWeapon(weapon.Weapon):

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.name = 'Magic Weapon'
        self.magic = True

        self.rdmg = 0
        self.cooldown = 5
