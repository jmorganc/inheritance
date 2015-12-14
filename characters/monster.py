from abc import ABCMeta, abstractmethod
from characters import character

class Monster(character.Character):

    @abstractmethod
    def __init__(self, name='Monster'):
        super().__init__()

        self.name = name
