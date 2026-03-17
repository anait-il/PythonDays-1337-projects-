from typing import List, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self) -> None:
        self.cards: List = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards[0]

    def get_deck_stats(self) -> Dict:
        creature = [card
                    for card in self.cards
                    if isinstance(card, CreatureCard)]
        spells = [card
                  for card in self.cards
                  if isinstance(card, SpellCard)]
        artifact = [card
                    for card in self.cards
                    if isinstance(card, ArtifactCard)]
        avg_cost = float(sum(card.cost for card in self.cards))
        return {
            'total_cards': len(self.cards),
            'creatures': len(creature),
            'spells': len(spells),
            'artifacts': len(artifact),
            'avg_cost': avg_cost
        }
