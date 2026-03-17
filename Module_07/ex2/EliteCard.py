from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.atack = attack
        self.health = health
        self.mana = 0
        self.type = 'Elite'

    def play(self, game_state: Dict) -> Dict:
        game_state['mana'] -= self.cost
        return {
            'card_playes': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack(self, target: str) -> Dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.atack,
            'combat_type': 'melee'
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'target': targets,
            'mana_used': self.cost
        }

    def defend(self, incoming_damage: int) -> Dict:
        damage_blocked = min(self.health, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        alive = self.mana - damage_taken > 0
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': alive
        }

    def get_combat_stats(self) -> Dict:
        return {
            'attack': self.atack,
            'health': self.health,
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            'mana': self.mana,
            'cost': self.cost
        }
