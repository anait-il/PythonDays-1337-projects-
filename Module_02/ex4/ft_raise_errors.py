
class PlantError(Exception):
    pass


class WaterError(Exception):
    pass


class SunError(Exception):
    pass


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise PlantError("Plant name cannot be empty!")
    if water_level > 10:
        raise WaterError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise WaterError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise SunError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise SunError(f"Sunlight hour {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    print(check_plant_health("Tomato", 7, 10))

    try:
        print("\nTesting empty plant name...")
        print(check_plant_health("", 7, 10))
    except PlantError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad water level...")
        print(check_plant_health("Tomato", 15, 10))
    except WaterError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting bad sunlight hours...")
        print(check_plant_health("Tomato", 7, 0))
    except SunError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")
