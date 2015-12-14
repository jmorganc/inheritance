from abc import ABCMeta, abstractmethod


class Weapon(metaclass=ABCMeta):

    name = 'Weapon'
    level = 0

    ddmg = 0
    rdmg = 0
    mdmg = 0

    acc = 0

    cooldown = 0


    @abstractmethod
    def __init__(self):
        pass
