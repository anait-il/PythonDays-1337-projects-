

class GardenError(Exception):
    """for garden problems"""

    def __init__(self, msg: str):
        super().__init__(msg)


class PlantError(GardenError):
    """for plant problems"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class WaterError(GardenError):
    """for water problems"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def ft_custom_errors() -> None:
    """test my custom exceptions"""

    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")
