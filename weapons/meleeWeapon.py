from abc import ABCMeta, abstractmethod
from weapons import weapon

class MeleeWeapon(weapon.Weapon):

    name = 'Melee Weapon'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.cooldown = 2.5
