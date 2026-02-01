
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self):
        print(f"{self.name} (Flower): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: str = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides", end=" ")
        print(f"{(self.trunk_diameter * 1.56):.0f} square meter of shade")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def veg_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def print_obj(flower_obj: list[Flower],
              tree_obj: list[Tree],
              veg_obg: list[Vegetable]) -> None:
    print("")
    for i in flower_obj:
        i.bloom()
    print("")
    for j in tree_obj:
        j.produce_shade()
    print("")
    for z in veg_obg:
        z.veg_info()


def plant_types() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 10, 30, "Red")
    sunflower = Flower("Sunflower", 150, 45, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 600, 2500, 60)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 60, "Autumn", "vitamin A")

    flower_obj: list[Flower] = [rose, sunflower]
    vegetable_obj: list[Vegetable] = [tomato, carrot]
    tree_obj: list[Tree] = [oak, maple]
    print_obj(flower_obj, tree_obj, vegetable_obj)


if __name__ == "__main__":
    plant_types()
