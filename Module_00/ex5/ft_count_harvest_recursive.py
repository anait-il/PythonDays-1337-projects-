def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    day: int = 1

    def recursive_func(days, day) -> None:
        if day > days:
            return
        print(f"day {day}")
        recursive_func(days, day + 1)

    recursive_func(days, day)
    print("Harvest time!")
