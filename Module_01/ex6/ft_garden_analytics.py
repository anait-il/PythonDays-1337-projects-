
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.type: str = "regular"
        self.growth: int = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1
        print(f"{self.name}: grew 1cm")

    def info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.type: str = "flowering"

    def info(self) -> None:
        print(f"- {self.name}: {self.height}cm,", end="")
        print(f" {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize: int = prize
        self.type: str = "prize flowers"

    def info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} ", end="")
        print(f"flowers (blooming), Prize points: {self.prize}")


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list[Plant] = []
        self.plant_added: int = 0
        self.total_height: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.plant_added += 1
        print(f"Added {plant.name} to {self.name}'s garden")


class GardenManager:

    gardens: list[Garden] = []

    def total_gardens(garden: list[Garden]) -> int:
        total: int = 0
        for i in garden:
            total += 1
        return total
    total_gardens = staticmethod(total_gardens)

    def print_intro() -> None:
        print("=== Garden Management System Demo ===\n")
    print_intro = staticmethod(print_intro)

    def create_garden_network(cls, garden: list[Garden]) -> None:
        cls.gardens += [garden]
        cls.garden_growth(garden)
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:
        def __init__(self, garden: Garden) -> None:
            self.garden: Garden = garden
            self.plants_count: int = garden.plant_added
            self.total: int = 0
            self.regular_count: int = 0
            self.flowering_count: int = 0
            self.prize_count: int = 0
            for plant in garden.plants:
                self.total += plant.growth
                if plant.type == "regular":
                    self.regular_count += 1
                elif plant.type == "flowering":
                    self.flowering_count += 1
                elif plant.type == "prize flowers":
                    self.prize_count += 1

        def count_plants(flowering_count: int,
                         prize_count: int,
                         regular_count: int,
                         total: int,
                         plants_count: int) -> None:
            print(f"\nPlants added: {plants_count}, Total growth: {total}cm")
            print(f"Plant types: {regular_count} regular, ", end="")
            print(f"{flowering_count} flowering, {prize_count} prize flowers")
            print("")
        count_plants = staticmethod(count_plants)

    def height_validation(cls) -> None:
        for garden in cls.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    print("Height validation test: False")
                    return
        print("Height validation test: True")
    height_validation = classmethod(height_validation)

    def Scores(cls) -> None:
        print("Garden scores - ", end="")

        first: bool = True
        for garden in cls.gardens:
            for plant in garden.plants:
                garden.total_height += plant.height
            if not first:
                print(", ", end="")
            print(f"{garden.name}: {garden.total_height}", end="")
            first = False

        print("")
    Scores = classmethod(Scores)

    def garden_repport(cls) -> None:
        for x in cls.gardens:
            if x.plants == []:
                break
            print(f"=== {x.name}'s Garden Report ===")
            print("Plants in garden:")
            for plant in x.plants:
                plant.info()
            stats = cls.GardenStats(x)
            stats.count_plants(stats.flowering_count,
                               stats.prize_count,
                               stats.regular_count,
                               stats.total,
                               stats.plants_count)
    garden_repport = classmethod(garden_repport)

    def garden_growth(cls, garden: list[Garden]) -> None:
        if garden.plants == []:
            return
        print(f"{garden.name} is helping all plants grow...")
        for plant in garden.plants:
            plant.grow()
    garden_growth = classmethod(garden_growth)


if __name__ == "__main__":
    GardenManager.print_intro()

    Alice = Garden("Alice")
    Bob = Garden("Bob")

    Alice.add_plant(Plant("Oak tree", 20))
    Alice.add_plant(FloweringPlant("Rose", 15, "Red"))
    Alice.add_plant(PrizeFlower("Sunflowers", 51, "Yellow", 10))

    my_garden: list[Garden] = [Alice, Bob]
    print("")
    first: bool = True
    for garden in my_garden:
        if not first:
            print("")
        GardenManager.create_garden_network(garden)
        first = False
    print("")

    GardenManager.garden_repport()
    GardenManager.height_validation()
    GardenManager.Scores()
    print("Total gardens managed: ", end="")
    print(f"{GardenManager.total_gardens(GardenManager.gardens)}")
