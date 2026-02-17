
def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> str:
    """cheack the health of plants"""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hour {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    print(check_plant_health("Tomato", 7, 10))

    try:
        print("\nTesting empty plant name...")
        print(check_plant_health("", 7, 10))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)

    try:
        print("\nTesting bad water level...")
        print(check_plant_health("Tomato", 15, 10))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)

    try:
        print("\nTesting bad sunlight hours...")
        print(check_plant_health("Tomato", 7, 0))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
