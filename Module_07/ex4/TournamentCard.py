from typing import Dict
import random

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 card_id: str,
                 power: int,
                 rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.power = power
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: Dict) -> Dict:
        return {
                "card": self.name,
                "action": "played"}

    def attack(self, target: "TournamentCard") -> Dict:
        if self.power > target.power:
            return {'winner': self, 'loser': target}
        elif self.power < target.power:
            return {'winner': target, 'loser': self}

        else:
            wins = random.choice([self, target])
            loser = self if wins is self else target

            return {'winner': wins, 'loser': loser}

    def defend(self, incoming_damage: int) -> Dict:
        return {
            'card': self.name,
            'damage': incoming_damage
        }

    def get_combat_stats(self) -> Dict:
        return {
            'id': self.card_id,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.new_rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.new_rating = self.calculate_rating()

    def get_rank_info(self) -> Dict:
        return {
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }
