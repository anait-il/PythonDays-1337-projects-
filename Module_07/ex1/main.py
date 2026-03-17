from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
import random


def main() -> None:
    try:
        print()
        print("=== DataDeck Deck Builder ===")
        print()
        print("Building deck with different card types...")

        dragon = CreatureCard("fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        effect_type = ['damage', 'heal', 'buff', 'debuff']
        bolt = SpellCard('Lightning Bolt',
                         3,
                         Rarity.EPIC.value,
                         random.choice(effect_type))
        crystal = ArtifactCard("Mana Crystal", 2, Rarity.EPIC.value, 3)

        deck = Deck()
        cards = [dragon, bolt, crystal]
        for card in cards:
            deck.add_card(card)
        print(f"Deck stats: {deck.get_deck_stats()}")
        print()
        print("Drawing and playing cards:")
        print()
        game_stat = {
            'mana': 20
        }
        deck.shuffle()
        while deck.cards:
            try:
                card = deck.draw_card()
                print(f"Drew: {card.name} ({card.type})")
                print(f"Play result: {card.play(game_stat)}")
                deck.remove_card(card.name)
                print()
            except ValueError as e:
                print(f"ERROR: {e}")
                deck.remove_card(card.name)
                print()

        print("Polymorphism in action: Same interface, ", end="")
        print("different card behaviors!")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
