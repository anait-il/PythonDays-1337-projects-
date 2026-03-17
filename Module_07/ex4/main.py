
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()
    cards = [
        TournamentCard("Fire Dragon",
                       5,
                       Rarity.LEGENDARY.value,
                       "dragon_001",
                       8),
        TournamentCard("Ice Wizard", 4, Rarity.EPIC.value, "wizard_001", 6)
    ]

    print("Registering Tournament Cards...")
    print()
    for card in cards:
        info = platform.register_card(card)
        print(f"{info}:")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    idx = 1
    for card in leaderboard:
        print(
            f"{idx}. {card.name} \
            - Rating: {card.new_rating} ({card.wins}-{card.losses})")
        idx += 1
    print()

    report = platform.generate_tournament_report()
    print("Platform Report:")
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    try:
        main()
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"ERROR: {e}")
