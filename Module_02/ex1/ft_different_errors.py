

def garden_operations(error: str) -> None:
    """Demonstrate different types of python errors"""

    if error == "valueError":
        print("Testing ValueError...")
        print("my age is {:d}" .format('abc'))

    elif error == "zerodivision":
        print("Testing ZeroDivisionError...")
        nb: int = 15 / 0
        print(nb)

    elif error == "filenotfound":
        print("Testing FileNotFoundError...")
        f = open("file.txt")
        f.close("file.txt")

    elif error == "keyerror":
        print("Testing KeyError...")
        garden: dict = {"tomato": 5,
                        "botato": 4,
                        "carrot": 3}
        print(garden["onion"])


def test_error_types() -> None:
    """Catch the errors by calling the garden function"""

    print("=== Garden Error Types Demo ===\n")

    errors: list[str] = ["valueError",
                         "zerodivision",
                         "filenotfound",
                         "keyerror"]
    for error in errors:
        try:
            garden_operations(error)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'file.txt'\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except KeyError:
            print("Caught KeyError: 'onion'\n")
        except Exception as e:
            print(e)

    try:
        print("Testing multiple errors together...")
        dic: dict = {"hello": 0}
        print(dic["world"])
        f = open("test.txt")
        f.close("test.txt")
        number: int = 100 / 0
        print(number)
        print(f"{'abc':d}")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    except Exception as e:
        print(e)

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(e)
