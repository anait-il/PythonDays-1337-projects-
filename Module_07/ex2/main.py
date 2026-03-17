from ex2.EliteCard import EliteCard
from ex0.Card import Rarity


def main() -> None:
    try:
        print()
        print("=== DataDeck Ability System ===")
        print()
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
        print()
        player = 'Arcane Warrior'
        print(f'Playing {player} (Elite Card):')
        print()
        print('Combat phase:')
        elite = EliteCard(player, 4, Rarity.ELITE, 5, 3)
        game_stat = {
            'mana': 4
        }

        elite.mana = game_stat['mana']
        print(f"Attack result: {elite.attack('Enemy')}")
        print(f"Defense result: {elite.defend(5)}")
        print()
        print("Magic phase:")
        print("Spell cast: ", end="")
        print(f"{elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
        print(f"Mana channel: {elite.channel_mana(3)}")
        print()
        print('Multiple interface implementation successful!')
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
