
class SecurePlanet:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0

    def set_height(self, height: int) -> int:
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}", end="")
            print("cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return 0
        else:
            self._height = height
            return 1

    def set_age(self, age: int) -> int:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}", end="")
            print(" days [REJECTED]")
            print("Security: Negative age rejected\n")
            return 0
        else:
            self._age = age
            return 1

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlanet("Rose")
    print(f"Plant created: {plant.name}")
    age: int = plant.set_age(2)
    height: int = plant.set_height(100)
    if age == 1:
        print(f"Age updated: {plant.get_age()} days [OK]")
    if height == 1:
        print(f"Height updated: {plant.get_height()}cm [OK]")
    print(f"\nCurrent plant: {plant.name} ", end="")
    print(f"({plant._height}cm, {plant._age} days)")


if __name__ == "__main__":
    ft_garden_security()
