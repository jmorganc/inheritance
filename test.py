#!/usr/bin/python3

import sys

from characters.rockMonster import RockMonster
from characters.warriorPlayer import WarriorPlayer
from weapons.sword import Sword
from weapons.bow import Bow
from weapons.wand import Wand


def main():
    myWarrior = WarriorPlayer('Brutus')
    myWarrior.gear['weapon'] = Sword()

    enemy = RockMonster()

    battle(myWarrior, enemy)


def battle(attacker, target):
    """
    Exchange attacks until someone is dead
    """
    while not attacker.isDead() and not target.isDead():
        battleStatus(attacker, target)

        attacker.attack(target)
        if target.isDead():
            print('{} has defeated {}!'.format(attacker.name, target.name))
            return

        target.attack(attacker)
        if attacker.isDead():
            print('{} has defeated {}!'.format(target.name, attacker.name))
            return


def battleStatus(attacker, target):
    print('{}\'s HP: {}/{}. {}\'s HP: {}/{}'.format(attacker.name, attacker.hp, attacker.hp_max, target.name, target.hp, target.hp_max))


if __name__ == '__main__':
    sys.exit(main())
