class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


first_plant = Plant("Rose", 25, 15)
secont_plant = Plant("Sunflower", 80, 45)
third_plant = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    first_plant.print_info()
    secont_plant.print_info()
    third_plant.print_info()
