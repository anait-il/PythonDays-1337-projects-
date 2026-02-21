players: dict = {
    "alice": {'score': 2300,
              'status': 'active',
              'achievements': ('killed monster',
                               'found treasure',
                               'leveled up',
                               'treasure_seeker',
                               'boss_hunter'),
              'region': "north"
              },
    "bob":   {'score': 1850,
              'status': 'active',
              'achievements': ('killed monster',
                               'combo_king',
                               'explorer'),
              'region': "east"
              },
    "charlie":   {'score': 2100,
                  'status': 'active',
                  'achievements': ('leveled up',
                                   'treasure_seeker'),
                  'region': "central"
                  },
    "diana":   {'score': 500,
                'status': 'inactive',
                'achievements': ('found treasure',),
                'region': "west"
                }
}


def list_comp() -> None:
    print("=== List Comprehension Examples ===")
    hight_score: list = [player
                         for player in players
                         if players[player]['score'] > 2000]
    print(f"Hight scores (>2000): {hight_score}")

    scores_doubled: list = [players[player]['score'] * 2 for player in players]
    print(f"Scores doubled: {scores_doubled}")

    active_palyers: list = [player
                            for player in players
                            if players[player]['status'] == 'active']
    print(f"Active players: {active_palyers}\n")


def dict_comp() -> None:
    players_score: dict = {player: players[player]['score']
                           for player in players}
    print(f"Player scores: {players_score}")

    categories: list = ['hight' if players[player]['score'] > 2000
                        else 'medium' if players[player]['score'] > 1500
                        else 'low'
                        for player in players]
    score_categorie: dict = {categorie: sum(1 for c in categories
                                            if c == categorie)
                             for categorie in categories}
    print(f"Score categorie: {score_categorie}")

    achievements_count: dict = {player: len(players[player]['achievements'])
                                for player in players}
    print(f"Achievements regions: {achievements_count}")


def set_comp() -> None:
    unique_players: set = {player for player in players}
    print(f"Unique players: {unique_players}")

    achievements: list = []
    for player in players:
        for item in players[player]['achievements']:
            achievements += [item]
    score_achiev: set = {item for item in achievements}
    print(f"Unique achievements: {score_achiev}")

    active_regions: set = {players[player]['region']
                           for player in players
                           if players[player]['status'] == 'active'}
    print(f"Active regions: {active_regions}")


def analytics() -> None:
    total_players: int = len(players)
    print(f"Total players: {total_players}")

    achievements: list = []
    for player in players:
        for item in players[player]['achievements']:
            achievements += [item]
    total_unique_achievments: set = {item for item in achievements}
    print(f"Total unique achievements: {len(total_unique_achievments)}")

    scores: list = [players[player]['score'] for player in players]
    average_score: float = sum(scores) / total_players
    print(f"Average scores: {average_score}")

    top_perform: int = max(scores)
    player: list = [player
                    for player in players
                    if players[player]['score'] == top_perform]
    print(f"Top performer: {player[0]} ({players[player[0]]['score']}", end="")
    print(f" pointes, {len(players[player[0]]['achievements'])} achievements)")


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    list_comp()

    print("=== Dict Comprehension Examples ===")
    dict_comp()

    print("\n=== Set Comprehension Examples ===")
    set_comp()

    print("\n=== Combined Analysis ===")
    analytics()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
