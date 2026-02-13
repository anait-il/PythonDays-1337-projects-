
import sys


def current_inventory(dic: dict, total_item: int) -> dict:
    i: int = 0
    sort_dic: dict = dict()
    tmp_dic: dict = {k: v for k, v in dic.items()}
    
    while i < len(tmp_dic):
        key: str = ""
        value: int = 0
        for k, v in tmp_dic.items():
            if v > value:
                value = v
                key = k
        tmp_dic[key] = 0
        sort_dic[key] = value
        i += 1
    for k, v in sort_dic.items():
        print(f"{k}: {v} units ({(v * 100) / total_item:.1f}%)")
    return (sort_dic)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
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
        print("######", dic)
        sort_dict: dict = current_inventory(dic, total_item)
        print("######", dic)

        print("\n=== Inventory Statistics ===")
        keys: list = sort_dict.keys()
        for key, value in sort_dict.items():
            f_dic: dict = dict({key: value})
            break
        print(f"Most aabundant: {f_dic}")
        for key, value in sort_dict.items():
            lst_dic: dict = dict({key: value})
        print(f"Least aabundant: {lst_dic}")

        print("\n=== Management Suggestions ===")
        restock_needed: list = []
        for key, value in sort_dict.items():
            if value == 1:
                restock_needed += [key]
        print(f"Restock needed: {restock_needed}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(dic.keys())}")
        print(f"Dictionary values: {list(dic.values())}")
        inventory_search: str = "sword"
        print(f"Sample lookup - '{inventory_search}'", end=" ")
        print(f"in inventory: {dic[inventory_search]}")
