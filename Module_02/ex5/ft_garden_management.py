
class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunlightHoursError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        self.name: str = name
        self.water: int = water
        self.sunlight: int = sunlight


class GardenManager:
    def __init__(self, name: str, tank: int) -> None:
        self.name: str = name
        self.plants: list[Plant] = []
        self.tank: int = tank

    def add_plants(self, plant: Plant) -> None:
        try:
            if not plant.name or plant.name.__class__.__name__ != "str":
                raise PlantNameError("Plant name cannot be empty!")
            else:
                self.plants += [plant]
                print(f"Added {plant.name} successfully")
        except PlantNameError as e:
            print(f"Error: {e}")

    def watering_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if not plant.name or plant.name.__class__.__name__ != "str":
                    raise PlantNameError("Cannot water None - invalid plant!")
                print(f"Watering {plant.name} - success")
                self.tank -= plant.water
        except PlantNameError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def plant_health(self, plants: list[Plant]) -> None:
        try:
            for plant in plants:
                if plant.water > 10:
                    raise WaterLevelError(
                        f"Water level {plant.water} is too high (max 10)")
                if plant.water < 1:
                    raise WaterLevelError(
                        f"Water level {plant.water} is too low (min 2)")
                if plant.sunlight < 2:
                    raise SunlightHoursError(
                        f"Sunlight hours {plant.sunlight} is too low (min 2)")
                if plant.sunlight > 12:
                    raise SunlightHoursError(
                        f"Sunlight hours {plant.sunlight} is too high (max 12)"
                        )
                print(f"{plant.name}: healthy (water: {plant.water},", end=" ")
                print(f"sun: {plant.sunlight})")
        except GardenError as e:
            print(f"Error checking {plant.name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden: GardenManager = GardenManager("garden", 20)
    plant1: Plant = Plant("tomato", 5, 8)
    plant2: Plant = Plant("lettuce", 15, 9)
    plant3: Plant = Plant("", 10, 10)
    plant_obj: list[Plant] = [plant1, plant2, plant3]

    print("\nAdding plants to garden...")

    for plant in plant_obj:
        garden.add_plants(plant)

    print("\nWatering plants...")
    garden.watering_plants()

    print("Checking plant health...")
    garden.plant_health(garden.plants)

    print("\nTesting error recovery...")
    try:
        if garden.tank == 0:
            raise GardenError(" Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
