#!/usr/bin/python3

import sys
import threading

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

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    """
    t = threading.Thread(target=_threaded_attack, args=(attacker, target))
    t.start()

    t = threading.Thread(target=_threaded_attack, args=(target, attacker))
    t.start()
    t.join()


def _threaded_attack(attacker, target):
    while target.is_alive() and attacker.is_alive():
        attacker.attack(target)
        if not target.is_alive():
            print('{} has defeated {}!'.format(attacker.name, target.name))
            return


def battle_status(attacker, target):
    print('{}\'s HP: {}/{}. {}\'s HP: {}/{}'.format(attacker.name, attacker.hp, attacker.hp_max, target.name, target.hp, target.hp_max))


if __name__ == '__main__':
    sys.exit(main())
