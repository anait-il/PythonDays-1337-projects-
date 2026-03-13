from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self) -> None:
        self.__attack = 0
        self.__health = 0

    def play(self, game_state: dict) -> None:
        pass

    def attack_target(self) -> None:
        pass

    def set_attheal(self, attack, health) -> None:
        if attack >= 0:
            self.__attack = attack
        else:
            raise ValueError("attack is not valid")
        if health >= 0:
            self.__health = health
        else:
            raise ValueError("health is not valid")
    
    def get_atheal(self, attack, health) ->Dict[str, int]:
        return {
            "attack": self.__attack,
            "health": self.__health
        }