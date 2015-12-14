from abc import ABCMeta, abstractmethod
from characters import character

class Monster(character.Character):

    @abstractmethod
    def __init__(self):
        super().__init__()
