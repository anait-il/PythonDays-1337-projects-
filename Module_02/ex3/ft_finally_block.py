

def water_plants(plant_list: list) -> None:
    """Waterig the plants"""
    print("Opening watering system")
    if not plant_list:
        raise ValueError("Cannot water None - invalide plant!")
    for plant in plant_list:
        if not plant:
            raise ValueError("Cannot water None - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system() -> None:
    """Test the plant watering"""
    print("=== Garden Watering System ===")
    flag: int = 0
    try:
        print("\nTesting normal watering...")
        plant: list = ["tomato", "lettuce", "carrots"]
        water_plants(plant)
    except ValueError as e:
        flag = 1
        print(f"Errr: {e}")
    finally:
        print("Closing watering system (cleanup)")
        if flag == 0:
            print("Watering completed successfully")

    flag == 0
    try:
        print("\nTesting with error...")
        plant2: list = ["tomato", None, "botato"]
        water_plants(plant2)
    except ValueError as e:
        flag = 1
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
        if flag == 0:
            print("Watering completed successfully")

    print("\nCleanup always happens, even with errors!")
