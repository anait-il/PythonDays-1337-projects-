
import sys


def current_inventory(dic: dict, total_item: int) -> dict:
    i: int = 0
    sort_dic: dict = dict()
    new_dic = {k: v for k, v in dic.items()}

    while i < len(new_dic):
        key: str = ""
        value: int | None = None
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
        if len(sys.argv) > 1:
            print("=== Inventory System Analysis ===")
            flag: bool = True
            dic: dict = dict()
            i: int = 1
            while i < len(sys.argv):
                try:
                    parts: list = sys.argv[i].split(":")
                    if len(parts) != 2 or not parts[1]:
                        i += 1
                        print(f"Error: key '{parts[0]}' without value")
                        flag = False
                        continue
                    if int(parts[1]) < 0:
                        i += 1
                        print(f"Error: key '{parts[0]}' with negative value")
                        flag = False
                        continue
                    dic[parts[0]] = int(parts[1])
                    i += 1
                except Exception as e:
                    print(f"Error: {e}\n")
                    i += 1
            if not flag:
                print()

            total_item: int = 0
            item: int = 0
            for value in dic.values():
                total_item += value
                item += 1
            print(f"Total items in inventory: {total_item}")
            print(f"Unique item types: {item}")

            if dic:
                print("\n=== Current Inventory ===")
                sort_dict: dict = current_inventory(dic, total_item)

                print("\n=== Inventory Statistics ===")
                for key, value in sort_dict.items():
                    f_dic: dict = dict({key: value})
                    break
                (k, v), = f_dic.items()
                print(f"Most abundant: {k} ({v} unit{'s' if v > 1 else ''})")
                for key, value in sort_dict.items():
                    lst_dic: dict = dict({key: value})
                (k, v), = lst_dic.items()
                print(f"Least abundant: {k} ({v} unit{'s' if v > 1 else ''})")

                print("\n=== Item Categories ===")
                abundance_dictionary: dict = {"abundant": {},
                                              "moderate": {},
                                              "scarce": {}}
                for k, v in sort_dict.items():
                    if v > 5:
                        abundance_dictionary["abundant"].update({k: v})
                    elif 3 < v <= 5:
                        abundance_dictionary["moderate"].update({k: v})
                    elif v <= 3:
                        abundance_dictionary["scarce"].update({k: v})
                if len(abundance_dictionary["abundant"]) > 0:
                    print(f"Abundant: {abundance_dictionary.get('abundant')}")
                print(f"Moderate: {abundance_dictionary.get('moderate')}")
                print(f"Scarce: {abundance_dictionary.get('scarce')}")

                print("\n=== Management Suggestions ===")
                restock_needed: list = []
                for key, value in sort_dict.items():
                    if value <= 1:
                        restock_needed += [key]
                restock: str = ""
                i = 0
                for key in restock_needed:
                    restock += (
                        f"{key}{', ' if i < (len(restock_needed) - 1) else ''}"
                        )
                    i += 1
                print(f"Restock needed: {restock}")

                print("\n=== Dictionary Properties Demo ===")
                dic_keys: str = ""
                dic_val: str = ""
                i = 0
                for key, value in dic.items():
                    dic_keys += (
                        f"{key}{', ' if i < (len(dic.keys()) - 1) else ''}"
                        )
                    dic_val += (
                        f"{value}{', ' if i < (len(dic.values()) - 1) else ''}"
                        )
                    i += 1
                print(f"Dictionary keys: {dic_keys}")
                print(f"Dictionary values: {dic_val}")
                inventory_search: str = "sword"
                print(f"Sample lookup - '{inventory_search}'", end=" ")
                print(f"in inventory: {inventory_search in dic}")

    except Exception as e:
        print(f"Error: {e}")
