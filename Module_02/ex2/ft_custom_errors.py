
class GardenError(Exception):
    """for garden problems"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class PlantError(GardenError):
    """for plant problems"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class WaterError(GardenError):
    """for water problems"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def test_planterror() -> None:
    """raise plant error"""
    print("Testing PlantError...")
    raise PlantError("The tomato plant is wilting!")


def test_watererror() -> None:
    """raise water error"""
    print("Testing WaterError...")
    raise WaterError("Not enough water in the tank!")


def test_gardenerror(flag: int) -> None:
    """
    raise any error and it well be catched by gardenrerror exception class
    """

    if flag == 1:
        raise WaterError("Not enough water in the tank!")
    elif flag == 0:
        raise PlantError("The tomato plant is wilting!")


def ft_custom_errors() -> None:
    """test my custom exceptions"""

    print("=== Custom Garden Errors Demo ===\n")
    try:
        test_planterror()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        test_watererror()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        test_gardenerror(0)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        test_gardenerror(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
