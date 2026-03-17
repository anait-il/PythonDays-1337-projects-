from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    ELITE = "ELITE"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        if cost < 0:
            raise ValueError("cost must be positive")
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: Dict) -> None:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> Dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False
