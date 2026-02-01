class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def print_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def factory_pattern(plant_data: list[tuple[str, int, int]]) -> list[Plant]:
    return [Plant(name, height, age) for name, height, age in plant_data]


def plants_factory() -> int:
    plant_data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Oak", 200, 365),
        ("Fern", 15, 120)
    ]
    buffer: list[Plant] = factory_pattern(plant_data)
    i: int = 0
    for plant in buffer:
        plant.print_info()
        i += 1
    return i


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    i: int = plants_factory()
    print("\nTotal plants created:", i)
