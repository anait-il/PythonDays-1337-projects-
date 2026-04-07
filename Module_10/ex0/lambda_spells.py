

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    art_sorted = sorted(artifacts, key=lambda m : m['power'], reverse=True)
    return art_sorted


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    power_mages = filter(lambda m : m['power'] >= min_power, mages)
    return power_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = map(lambda m : '* ' + m + ' *', spells)
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    stats = {}
    stats['max_power'] = max(mages, key=lambda m : m['power'])
    stats['min_power'] = min(mages, key=lambda m : m['power'])
    stats['avg_power'] = round(sum(map(lambda m : m['power'], mages)) / len(mages), 2)
    return stats


def main() -> None:
    artifacts = [{'name': 'Ice Wand', 'power': 82, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 102, 'type': 'armor'}]

    mages = [{'name': 'Nova', 'power': 84, 'element': 'ice'},
             {'name': 'Jordan', 'power': 33, 'element': 'shadow'},
             {'name': 'Alex', 'power': 703, 'element': 'wind'},
             {'name': 'Nova', 'power': 78, 'element': 'ice'},
             {'name': 'Riley', 'power': 75, 'element': 'earth'}]

    spells = ['fireball', 'tornado', 'blizzard', 'heal']
    try:
        print("Testing artifact sorter...")
        art_sorted = artifact_sorter(artifacts)
        print(f"{art_sorted[0]['name']} ({art_sorted[0]['power']} power) comes before {art_sorted[1]['name']} ({art_sorted[1]['power']} power)")
    except Exception as e:
        print('Error:', e)

    try:
        print("\nTesting power filter")
        min_power = 75
        mages_power = power_filter(mages, min_power)
        print(f'The mages with power more or equal than {min_power} is:')
        for mage in mages_power:
            print(f"{mage['name']} ({mage['power']} power)")
    except Exception as e:
        print('Error:', e)

    try:
        print("\nTesting spell transformer")
        result = spell_transformer(spells)
        for word in result:
            print(word, end=" ")
        print()
    except Exception as e:
        print('Error:', e)

    try:
        print('\nTesting mage stats')
        stats = mage_stats(mages)
        print(stats)
    except Exception as e:
        print('Error:', e)


if __name__ == "__main__":
    main()
