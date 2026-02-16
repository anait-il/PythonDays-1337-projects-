
import sys


def current_inventory(dic: dict, total_item: int) -> dict:
    i: int = 0
    sort_dic: dict = dict()
    new_dic = {k: v for k, v in dic.items()}

    while i < len(new_dic):
        key: str = ""
        value: int = None
        for k, v in new_dic.items():
            if (value is None or v > value) and k not in sort_dic.keys():
                value = v
                key = k
        sort_dic[key] = value
        i += 1
    for k, v in sort_dic.items():
        print(f"{k}: {v} units ({(v * 100) / total_item:.1f}%)")
    return (sort_dic)


if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        if len(sys.argv) > 1:
            try:
                dic: dict = dict()
                i: int = 1
                while i < len(sys.argv):
                    parts: list = sys.argv[i].split(":")
                    if len(parts) != 2 or not parts[1]:
                        i += 1
                        print(f"Error: key '{parts[0]}' without value")
                        continue
                    dic[parts[0]] = int(parts[1])
                    i += 1
            except Exception as e:
                print(f"Error: {e}\n")

            total_item: int = 0
            item: int = 0
            for value in dic.values():
                total_item += value
                item += 1
            print(f"Total items in inventory: {total_item}")
            print(f"Unique item types: {item}")

            print("\n=== Current Inventory ===")
            sort_dict: dict = current_inventory(dic, total_item)

            print("\n=== Inventory Statistics ===")
            for key, value in sort_dict.items():
                f_dic: dict = dict({key: value})
                break
            print(f"Most aabundant: {f_dic}")
            for key, value in sort_dict.items():
                lst_dic: dict = dict({key: value})
            print(f"Least aabundant: {lst_dic}")

            print("\n=== Item Categories ===")
            abundance_dictionary: dict = {"moderate": {}, "scarce": {}}
            for k, v in sort_dict.items():
                if v > 3:
                    abundance_dictionary["moderate"].update({k: v})
                elif v <= 3:
                    abundance_dictionary["scarce"].update({k: v})
            print(f"Moderate: {abundance_dictionary['moderate']}")
            print(f"Scarce: {abundance_dictionary['scarce']}")

            print("\n=== Management Suggestions ===")
            restock_needed: list = []
            for key, value in sort_dict.items():
                if value <= 1:
                    restock_needed += [key]
            print(f"Restock needed: {restock_needed}")

            print("\n=== Dictionary Properties Demo ===")
            dic_keys: list = [key for key in dic.keys()]
            dic_val: list = [value for value in dic.values()]
            print(f"Dictionary keys: {dic_keys}")
            print(f"Dictionary values: {dic_val}")
            inventory_search: str = "sword"
            print(f"Sample lookup - '{inventory_search}'", end=" ")
            print(f"in inventory: {dic.get(inventory_search) == True}")
    except Exception as e:
        print(e)
