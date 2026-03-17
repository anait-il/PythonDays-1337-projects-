from typing import Dict, Union
from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = 'Creature'
        self.set_attack(attack)
        self.set_health(health)

    def play(self, game_state: Dict) -> Dict[str, Union[str, int]]:
        if self.is_playable(game_state['mana']):
            game_state['mana'] -= self.cost
            return {
                'card_playes': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
        else:
            raise ValueError("this card not playable")

    def get_card_info(self) -> Dict[str, Union[str, int]]:
        info = super().get_card_info()
        info.update({'type': self.type,
                     'attack': self.attack_power,
                     'health': self.health})
        return info

    def attack_target(self) -> Dict[str, Union[str, int]]:
        return {
            'attacker': self.name,
            'target': 'Goblin Warrior',
            'damage_dealt': self.attack_power,
            'combat_resolved': True
        }

    def set_attack(self, attack: int) -> None:
        if attack >= 0:
            self.attack_power = attack
        else:
            raise ValueError("attack is not valid")

    def set_health(self, health: int) -> None:
        if health >= 0:
            self.health = health
        else:
            raise ValueError("health is not valid")
