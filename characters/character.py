from abc import ABCMeta, abstractmethod
from weapons import unarmed


class Character(metaclass=ABCMeta):

    hp = 0
    mp = 0

    ddef = 0
    rdef = 0
    mdef = 0

    str = 0
    int = 0
    dex = 0

    weapon = None


    @abstractmethod
    def __init__(self):
        self.hp = 5
        self.mp = 5

        self.str = 5
        self.int = 5
        self.dex = 5

        self.weapon = unarmed.Unarmed()


    def meleeAttack(self, target):
        print('Attack!')
        target.hp = target.hp - (1 * self.weapon.dmg)


    def rangedAttack(self, target):
        print('Attack!')
        target.hp = target.hp - (1 * self.weapon.rdmg)


    def magicAttack(self, target):
        print('Attack!')
        target.hp = target.hp - (1 * self.weapon.mdmg)


    def defend(self):
        print('Defend!')


    def isDead(self):
        if self.hp <= 0:
            return True

        return False
