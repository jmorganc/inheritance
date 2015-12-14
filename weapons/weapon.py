from abc import ABCMeta, abstractmethod


class Weapon(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.name = 'Weapon'
        self.level = 0

        self.ddmg = 0
        self.rdmg = 0
        self.mdmg = 0

        self.acc = 0

        self.cooldown = 0
