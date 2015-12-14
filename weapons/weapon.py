from abc import ABCMeta, abstractmethod


class Weapon(metaclass=ABCMeta):

    dmg = 0
    rdmg = 0
    mdmg = 0


    @abstractmethod
    def __init__(self):
        pass
