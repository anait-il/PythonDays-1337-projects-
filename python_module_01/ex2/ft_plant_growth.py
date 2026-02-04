class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.plant_age += 1


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 50, 15)
plants: list[Plant] = [rose, sunflower]
start_height: int = 0
for plant in plants:
    start_height += plant.height


def ft_plant_growth() -> None:
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    for x in range(6):
        for plant in plants:
            plant.age()
            plant.grow()
        if x == 5:
            print("=== Day 7 ===")
            for plant in plants:
                plant.get_info()
    end_height: int = 0
    for plant in plants:
        end_height += plant.height
    print(f"Growth this week: +{end_height - start_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
