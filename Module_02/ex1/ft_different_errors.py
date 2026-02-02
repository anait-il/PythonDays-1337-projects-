

def garden_operations() -> None:
    """Demonstrate different types of python errors"""

    try:
        print("Testing ValueError...")
        print("my age is {:d}" .format('abc'))

    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        nb: int = 15 / 0
        print(nb)

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("file.txt")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'file.txt'\n")

    try:
        print("Testing KeyError...")
        garden: dict = {"tomato": 5,
                        "botato": 4,
                        "carrot": 3}
        print(garden["onion"])

    except KeyError:
        print("Caught KeyError: 'onion'\n")


def test_error_types() -> None:
    """Catch the errors by calling the garden function"""

    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    try:
        print("Testing multiple errors together...")
        dic: dict = {"hello": 3}
        print(dic["world"])
        open("test.txt")
        number: int = 100 / 0
        print(number)
        print(f"{'abc':d}")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("\nAll error types tested successfully!")
