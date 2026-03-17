from ex0.Card import Card, Rarity
from typing import Dict, List, Any


class SpellCard(Card):

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.set_effect_type(effect_type)
        self.type = 'Spell'
        self.used = False

    def play(self, game_state: Dict) -> Dict:
        if self.is_playable(game_state['mana']):
            if self.used:
                raise ValueError("this card is already used")
            game_state['mana'] -= self.cost
            self.used = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": 'Deal 3 damage to target'}
        else:
            raise ValueError("this card not playable")

    def resolve_effect(self, targets: List) -> Dict[str, Any]:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
        }

    def set_effect_type(self, effect_type: str) -> None:
        effect_types = ['damage', 'heal', 'buff', 'debuff']
        if effect_type in effect_types:
            self.effect_type = effect_type
        else:
            raise ValueError("effect type doesn't match the required types")
