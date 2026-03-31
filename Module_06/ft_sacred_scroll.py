from alchemy import create_fire, create_water
import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.creatr_fire(): {create_fire()}")
    print(f"alchemy.elements.creatr_water(): {create_water()}")
    print(f"alchemy.elements.creatr_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.creatr_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_fire(): {alchemy.create_water()}")
    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


if __name__ == "__main__":
    try:
        main()
        print()
        print("Package metadata:")
        print(f"Version: {alchemy.__version__}")
        print(f"author: {alchemy.__author__}")
    except Exception as e:
        print(f"ERROR: {e}")
