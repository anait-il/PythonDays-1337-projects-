
import sys

print("=== Player Score Analytics ===")
argc: int = len(sys.argv)
if argc == 1:
    print("No scores provided. Usage: python3", end=" ")
    print("ft_score_analytics.py <score1> <score2> ...")
else:
    try:
        i: int = 1
        av: list = []
        while i < argc:
            av += [int(sys.argv[i])]
            i += 1
        totl_p: int = argc - 1
        total_s: int = sum(av)
        print(f"Scores processed: {av}")
        print(f"Total players: {totl_p}")
        print(f"Total score: {total_s}")
        print(f"Average score: {total_s / totl_p}")
        print(f"Hight score: {max(av)}")
        print(f"Low score: {min(av)}")
        print(f"Score range: {max(av) - min(av)}")
    except ValueError:
        print("Error: please enter a valid score")
    except Exception as obj:
        print(obj)
