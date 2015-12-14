from abc import ABCMeta, abstractmethod
from characters import character

class Monster(character.Character):

    name = 'Monster'

    @abstractmethod
    def __init__(self):
        pass
