
def check_temperature(temp_str: str) -> int:
    """chaeck the temperature is valid or not."""

    try:
        temp: int = int(temp_str)
        if temp >= 0 and temp <= 40:
            return temp
        elif temp > 40:
            raise ValueError(f"Error: {temp} is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"Error: {temp} is too cold for plants (min 0°C)")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


def test_temperature_input() -> None:
    """
    test the temperature function is it stil
    work even with non valid inputs.
    """

    tests: list[str] = ["25", "abd", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")

    for test in tests:
        print(f"Testing temperature: {test}")
        temp_check: int = check_temperature(test)
        if temp_check:
            print(f"Temperature {test}°C is perfect for plants!")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
