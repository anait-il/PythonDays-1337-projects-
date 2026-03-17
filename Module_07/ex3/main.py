from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:

    print("\n=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    if not result:
        return
    game_state = engine.get_engine_status()
    hand = ", ".join(f"{card.name} ({card.cost})" for card in engine.hand)
    print(f'Hand: [{hand}]')
    print()
    print("Turn execution:")
    print(f"strategy: {game_state['strategy_used']}")
    print(f"Actions: {result}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
