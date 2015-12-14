from abc import ABCMeta, abstractmethod
from weapons import weapon

class RangedWeapon(weapon.Weapon):

    name = 'Ranged Weapon'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.cooldown = 5
