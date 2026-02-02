

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        if plant_list is None:
            raise TypeError("Cannot water None - invalide plant!")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
        raise ValueError("Error")
    
    finally:
        print("Closing watering system (cleanup)")



def	test_watering_system() -> None:
    print("=== Garden Watering System ===")	
    try:
        print("\nTesting normal watering...")
        plant: list = ["tomato", "lettuce", "carrots"]
        water_plants(plant)
    except:
        pass
    else:
        print("Watering completed successfully")

    try:
        print("\nTesting with error...")
        plant2: list = ["tomato", None, "botato"]
        water_plants(plant2)
    except:
        pass
    else:
        print("Watering completed successfully")
    
    finally:
        print("\nCleanup always happens, even with errors!")



test_watering_system()

		

    