from abc import ABCMeta, abstractmethod
from weapons import weapon

class MagicWeapon(weapon.Weapon):

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.cooldown = 5
