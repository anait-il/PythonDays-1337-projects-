from ex0.Card import Card, Rarity
from typing import Dict


class ArtifactCard(Card):

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 durability: int) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.type = 'Artifact'
        self.effect = 'Permanent: +1 mana per turn'

    def play(self, game_state: Dict) -> Dict:
        if self.is_playable(game_state['mana']):
            game_state['mana'] -= self.cost
            game_state['mana'] += 1
            return {
                'name': self.name,
                'mana_used': self.cost,
                'effect': self.effect
            }
        else:
            raise ValueError("this card not playable")

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {
                'artifact': self.name,
                'status': 'artifact is broken'
            }
        self.durability -= 1
        return {
           'artifact': self.name,
           'effect': self.effect,
           'durability_left': self.durability,
           'status': 'artifact is work'
        }
