from abc import ABCMeta, abstractmethod
from characters import character

class Player(character.Character):

    @abstractmethod
    def __init__(self, name='Player'):
        super().__init__()

        self.name = name
        self.exp_max = self.level * 10
