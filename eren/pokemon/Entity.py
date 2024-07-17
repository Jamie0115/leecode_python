from abc import ABCMeta


class Pokemon(metaclass=ABCMeta):
    def __init__(self, name: str, level: int, hp: int, attack: int, defense: int):
        self.__name = name
        self.__level = level
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense


