
class Players:
    def __init__(self, name: str, achievements: set) -> None:
        self.name: str = name
        self.achievements: set = achievements

    def get_players(self) -> None:
        print(f"Player {self.name} achievements: {self.achievements}")


def unique_achievements(player: list) -> None:
    unique = set()
    for obj in player:
        unique = unique.union(obj.achievements)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")


def common_and_rare_achievements(players: list[Players]) -> None:
    common_all: set = players[0].achievements
    for obj in players:
        common_all = common_all.intersection(obj.achievements)
    print(f"Common to all players: {common_all}")

    p1 = players[0].achievements.difference(players[1].achievements,
                                            players[2].achievements)
    p2 = players[1].achievements.difference(players[0].achievements,
                                            players[2].achievements)
    p3 = players[2].achievements.difference(players[0].achievements,
                                            players[1].achievements)
    resault: set = p1 | p2 | p3
    print(f"Rare achievements (1 player): {resault}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player: list = ["Alice", "Bob", "charlie"]
    achievements: list[set] = [{'first_kill', 'level_10', 'treasure_hunter',
                                'speed_demon'},
                               {'first_kill', 'level_10', 'boss_slayer',
                                'collector'},
                               {'level_10', 'treasure_hunter', 'boss_slayer',
                                'speed_demon', 'perfectionist'}]
    objs: list = []
    i: int = 0
    while i < len(player):
        obj: Players = Players(player[i], achievements[i])
        obj.get_players()
        objs += [obj]
        i += 1

    print("\n=== Achievement Analytics ===")
    unique_achievements(objs)
    print("")
    common_and_rare_achievements(objs)
    s1: set = objs[0].achievements.intersection(objs[1].achievements)
    s2: set = objs[0].achievements.difference(objs[1].achievements)
    s3: set = objs[1].achievements.difference(objs[0].achievements)
    print(f"\nAlice vs Bob common: {s1}")
    print(f"Alice unique: {s2}")
    print(f"Bob unique: {s3}")
