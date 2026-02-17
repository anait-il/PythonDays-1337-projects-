
import math


def distance(coordinate: tuple, second_pointe: tuple) -> float:

    try:

        x, y, z = coordinate
        distance: float = math.sqrt((x - second_pointe[0])**2 +
                                    (y - second_pointe[1])**2 +
                                    (z - second_pointe[2])**2)
        return (distance)

    except Exception as e:

        raise e


def parsing(coor: str) -> tuple:

    try:

        parsed_position: list = coor.split(",")
        return tuple(int(item) for item in parsed_position)

    except Exception as e:

        raise e


def coordinate_system(coordinate_l: tuple, second_pointe: tuple) -> None:

    try:

        if coordinate_l.__class__ == tuple:
            print(f"Position created: {coordinate_l}")
            print(f"Distance between {second_pointe} and", end=" ")
            print(
                f" {coordinate_l}: {distance(coordinate_l, second_pointe):.2f}"
                )
        else:
            raise ValueError(f"Coordinate {coordinate_l} not valid")

    except Exception as obj:

        print(f"Error: {obj}")


def string_coordinat(coordinate_s: str, second_pointe: tuple) -> None:

    try:

        parsed_position: tuple = parsing(coordinate_s)
        des: float = distance(parsed_position, second_pointe)
        print(f"Parsing coordinates: \"{coordinate_s}\"")
        print(f"Parsed position: {parsed_position}")
        print(f"Distance between {second_pointe} and", end=" ")
        print(f"{parsed_position}: ", end="")
        print(f"{des:.1f}")

    except Exception as obj:

        print(f"Parsing invalid coordinates: \"{coordinate_s}\"")
        print(f"Error parsing coordinates: {obj}")
        print(f"Error details - type: {obj.__class__.__name__}", end=" ")
        print(f"Args: (\"{obj}\",)")


def unpacking(coor: tuple) -> None:
    print("Unpacking demonstration:")
    try:
        x, y, z = coor
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    print("=== Game Coordinate System ===")
    data: list = [(10, 20, 5), "3,4,0", "abc,def,ghi"]

    try:

        second_pointe: tuple = (0, 0, 0)
        for tupl in data:
            print("")
            if not tupl or tupl.__class__ == str:
                string_coordinat(tupl, second_pointe)
            else:
                coordinate_system(tupl, second_pointe)
        print("")
        unpacking((3, 4, 0))

    except Exception as e:

        print(e)
