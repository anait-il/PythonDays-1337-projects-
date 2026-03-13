from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> None:
        pass

    def get_card_info(self) -> None:
        pass

    def is_playable(self, available_mana: int):
        pass
