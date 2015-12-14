from abc import ABCMeta, abstractmethod
from weapons import unarmed
import time


class Character(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name='Character'):
        self.name = name
        self.level = 1

        self.hp_max = 1
        self.hp = 1
        self.mp_max = 1
        self.mp = 1

        self.ddef = 1
        self.mdef = 1
        self.rdef = 1

        self.str = 1
        self.int = 1
        self.dex = 1

        self.gear = {
            'head': None,
            'chest': None,
            'gloves': None,
            'pants': None,
            'boots': None,
            'ring': None,
            'necklace': None,
            'weapon': unarmed.Unarmed()
        }

        self.inventory_size = 1
        self.inventory = {}


    def attack(self, target):
        print('{} attacks {} with {}!'.format(self.name, target.name, self.gear['weapon'].name))

        if not target.is_alive():
            print('That target is already dead.')
            return

        if self.gear['weapon'].melee:
            damage_dealt = self._melee_attack()
        elif self.gear['weapon'].magic:
            damage_dealt = self._magic_attack()
        elif self.gear['weapon'].ranged:
            damage_dealt = self._ranged_attack()
        else:
            sys.exit('Unknown weapon type.')

        target.hp = target.hp - damage_dealt
        print('{} takes {} damage. ({}/{})\n'.format(target.name, damage_dealt, target.hp, target.hp_max))

        if target.is_alive():
            time.sleep(self.gear['weapon'].cooldown)

        return damage_dealt


    def _melee_attack(self):
        return self.gear['weapon'].ddmg


    def _magic_attack(self):
        return self.gear['weapon'].rdmg


    def _ranged_attack(self):
        return self.gear['weapon'].mdmg


    def defend(self):
        print('Defend!')


    def is_alive(self):
        if self.hp <= 0:
            return False

        return True


    def drop_items(self):
        if not is_alive:
            return inventory
