from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    try:
        print("\n=== DataDeck Card Foundation ===")
        print()
        print("Testing Abstract Base Class Design:")
        print()
        print("CreatureCard Info:")
        dragon = CreatureCard("fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        print(dragon.get_card_info())
        print()
        mana = {
            'mana': 6
        }
        print(f"Playing Fire Dragon with {mana['mana']} mana available:")
        is_playable = dragon.is_playable(mana['mana'])
        print(f"Playable: {is_playable}")
        try:
            print(f"Play result: {dragon.play(mana)}")
            print()
            print("Fire Dragon attacks Goblin Warrior:")
            print(f"Attack result: {dragon.attack_target()}")
        except ValueError as e:
            print(f"ERROR: {e}")
        print()
        print(f"Testing insufficient mana ({mana['mana']} available):")
        print(f"Playable: {dragon.is_playable(mana['mana'])}")
        print()
        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
