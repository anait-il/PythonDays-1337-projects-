
def check_temperature(temp_str: str) -> int:
    """chaeck the temperature is valid or not"""

    try:
        temp: int = int(temp_str)
        if temp >= 0 and temp <= 40:
            return temp
        elif temp > 40:
            return -1
        elif temp < 0:
            return -2
    except Exception:
        print(f"Error: {temp_str} is not a valide number")
        return -3


def test_temperature_input() -> None:
    """
    test the temperature function is it stil
    work even with non valid inputs
    """

    tests: list = ["25", "abd", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for test in tests:
        print(f"Testing temperature: {test}")
        temp_check: int = check_temperature(test)
        if temp_check == -3:
            print("")
            continue
        elif temp_check >= 0:
            print(f"Temperature {test}°C is perfect for plants!")
        elif temp_check == -1:
            print(f"Error: {test} is too hot for plants (max 40°C)")
        elif temp_check == -2:
            print(f"Error: {test} is too cold for plants (min 0°C)")
        print("")
    print("All tests completed - program didn't crash!")
