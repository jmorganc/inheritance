from abc import ABCMeta, abstractmethod
from weapons import unarmed


class Character(metaclass=ABCMeta):

    name = ''
    level = 1

    hp_max = 1
    hp = 1
    mp_max = 1
    mp = 1

    ddef = 1
    mdef = 1
    rdef = 1

    str = 1
    int = 1
    dex = 1

    gear = {
        'head': None,
        'chest': None,
        'gloves': None,
        'pants': None,
        'boots': None,
        'ring': None,
        'necklace': None,
        'weapon': unarmed.Unarmed()
    }

    inventory_size = 1
    inventory = {}


    @abstractmethod
    def __init__(self, name='Character'):
        self.name = name


    def battle(self, target):
        """
        Exchange attacks until someone is dead
        """
        while not self.isDead() or not target.isDead():
            self.attack(target)
            target.attack(self)


    def attack(self, target):
        print('{} attacks {} with {}!'.format(self.name, target.name, self.gear['weapon'].name))

        if target.isDead():
            print('That target is already dead.')
            return

        if self.gear['weapon'].melee:
            damage_dealt = self._meleeAttack(target)
        elif self.gear['weapon'].magic:
            damage_dealt = self._magicAttack(target)
        elif self.gear['weapon'].ranged:
            damage_dealt = self._rangedAttack(target)
        else:
            sys.exit('Unknown weapon type.')

        target.hp = target.hp - damage_dealt

        return damage_dealt


    def _meleeAttack(self, target):
        return self.gear['weapon'].ddmg


    def _rangedAttack(self, target):
        return self.gear['weapon'].rdmg


    def _rangedAttack(self, target):
        return self.gear['weapon'].mdmg


    def defend(self):
        print('Defend!')


    def isDead(self):
        if self.hp <= 0:
            return True

        return False


    def dropItems(self):
        if isDead:
            return inventory
