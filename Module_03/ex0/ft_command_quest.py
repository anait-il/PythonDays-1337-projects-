
import sys

total_args: int = len(sys.argv)
print("=== Command Quest ===")
if total_args == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {total_args}\n")
else:
    x: int = 0
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received : {total_args - 1}")
    for i in sys.argv:
        if x == 0:
            x += 1
            continue
        print(f"Argument {x}: {i}")
        x += 1
    print(f"Total arguments: {total_args}\n")
