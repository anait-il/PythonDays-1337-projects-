def ft_count_harvest_recursive(days=None, day=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print("day", day)
    ft_count_harvest_recursive(days, day+1)
