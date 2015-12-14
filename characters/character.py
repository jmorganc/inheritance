from abc import ABCMeta, abstractmethod
from weapons import unarmed


class Character(metaclass=ABCMeta):

    name = 'Character'
    level = 1

    hp = 1
    mp = 1

    ddef = 1
    rdef = 1
    mdef = 1

    str = 1
    int = 1
    dex = 1

    weapon = unarmed.Unarmed()
    inventory = {}


    @abstractmethod
    def __init__(self):
        pass


    def meleeAttack(self, target):
        print('Attack!')
        if target.isDead():
            print('That target is already dead.')
            return

        target.hp = target.hp - (1 * self.weapon.ddmg)


    def rangedAttack(self, target):
        print('Attack!')
        if target.isDead():
            print('That target is already dead.')
            return

        target.hp = target.hp - (1 * self.weapon.rdmg)


    def magicAttack(self, target):
        print('Attack!')
        if target.isDead():
            print('That target is already dead.')
            return

        target.hp = target.hp - (1 * self.weapon.mdmg)


    def defend(self):
        print('Defend!')


    def isDead(self):
        if self.hp <= 0:
            return True

        return False


    def dropItems(self):
        if isDead:
            return inventory
