import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_water
from alchemy.potions import strength_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print()
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()
    print("Method 2 - Specific function import:")
    print(f"craete_water(): {create_water()}")
    print()
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strengh_potion(): {strength_potion()}")


if __name__ == "__main__":
    try:
        main()
        print()
        print("All import transmutation methods mastered!")
    except Exception as e:
        print(f"ERROR: {e}")
