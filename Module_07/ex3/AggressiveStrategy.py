from typing import List, Dict
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0

        for card in hand:
            if card.cost <= 5 and isinstance(card, CreatureCard):
                cards_played.append(card)
                mana_used += card.cost

        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': mana_used,
            'targets_attacked': self.prioritize_targets(battlefield),
            'damage_dealt': sum(
                card.attack_power for card in cards_played
            )
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        target = [target
                  for target in available_targets
                  if isinstance(target, CreatureCard)]
        return (target if target else ['Enemy Player'])
