import random
from typing import Dict

from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card, Rarity


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int = None) -> Card:

        creatures = [
            ("Fire Dragon", 5, 7, 5),
            ("Goblin Warrior", 2, 3, 2),
            ("Elf Archer", 3, 4, 3)
        ]
        name, cost, attack, health = random.choice(creatures)
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power,
                                cost,
                                Rarity.LEGENDARY.value,
                                attack,
                                health)

        elif isinstance(name_or_power, int):
            return CreatureCard(name,
                                name_or_power,
                                Rarity.EPIC.value,
                                name_or_power,
                                name_or_power)

        return CreatureCard(name, cost, Rarity.EPIC.value, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        effect_types = ['damage', 'heal', 'buff', 'debuff']
        spells = [
            ('fire', 4, Rarity.EPIC.value, random.choice(effect_types)),
            ('Ice', 3, Rarity.EPIC.value, random.choice(effect_types)),
            ('Lightning', 5, Rarity.EPIC.value, random.choice(effect_types))
        ]

        name, cost, rarity, effect_type = random.choice(spells)
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, cost, rarity, effect_type)

        elif isinstance(name_or_power, int):
            return SpellCard(name, name_or_power, rarity, effect_type)

        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = [
            ('Rings', 3, Rarity.EPIC.value, 3),
            ('Staffs', 3, Rarity.EPIC.value, 3),
            ('Crystals', 3, Rarity.EPIC.value, 3)
        ]

        name, cost, rarity, durability = random.choice(artifacts)

        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, cost, rarity, durability)
        elif isinstance(name_or_power, int):
            return ArtifactCard(name, name_or_power, rarity, name_or_power)
        return ArtifactCard(name, cost, rarity, durability)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []

        creatures = []
        for _ in range(size // 3):
            creatures.append(self.create_creature())

        spells = []
        for _ in range(size // 3):
            spells.append(self.create_spell())

        artifacts = []
        for _ in range(size // 3):
            artifacts.append(self.create_artifact())
        deck = creatures + spells + artifacts
        return {
            'total_cards': size,
            'deck': deck
        }

    def get_supported_types(self) -> Dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
