from typing import Dict, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self,
                 number_card: int = 3,
                 battlefield: List = None,
                 turn: int = 0) -> None:
        if number_card < 3:
            raise ValueError("Invalid number of cards (min 3)")
        self.number = number_card
        self.hand = []
        self.battlefield = battlefield if battlefield else []
        self.turns_simulated = turn
        self.strategy_used = None
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        try:
            self.turns_simulated += 1
            hand = self.factory.create_themed_deck(self.number)
            hand = hand['deck']
            self.hand = hand
            self.cards_created = len(hand)
            turn_stats = self.strategy.execute_turn(hand, self.battlefield)
            self.strategy_used = self.strategy.get_strategy_name()
            self.total_damage = turn_stats['damage_dealt']
            return turn_stats
        except Exception as e:
            print(f"ERROR: {e}")

    def get_engine_status(self) -> Dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy_used,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
