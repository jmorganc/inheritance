from abc import ABCMeta, abstractmethod
from characters import character

class Player(character.Character):

    @abstractmethod
    def __init__(self, name='Player'):
        self.name = name
