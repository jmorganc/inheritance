import sys

from characters.rockMonster import RockMonster
from weapons.sword import Sword
from weapons.bow import Bow
from weapons.wand import Wand


def main():
    srmc_1 = RockMonster()
    srmc_2 = RockMonster()
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    print(srmc_1.gear['weapon'])
    srmc_1.meleeAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Sword()
    print(srmc_1.gear['weapon'])
    srmc_1.meleeAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Bow()
    print(srmc_1.gear['weapon'])
    srmc_1.rangedAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Wand()
    print(srmc_1.gear['weapon'])
    srmc_1.magicAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Wand()
    print(srmc_1.gear['weapon'])
    srmc_1.magicAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Wand()
    print(srmc_1.gear['weapon'])
    srmc_1.magicAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())

    srmc_1.gear['weapon'] = Wand()
    print(srmc_1.gear['weapon'])
    srmc_1.magicAttack(srmc_2)
    print(srmc_2.hp)
    print('Dead?', srmc_2.isDead())


if __name__ == '__main__':
    sys.exit(main())
