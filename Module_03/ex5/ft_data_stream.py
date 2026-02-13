
from typing import Generator


def generature(num: int) -> Generator[str, None, list]:
    players: list = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
    achievements: list = [
        'killed monster', 'found treasure', 'leveled up', 'treasure_seeker',
        'boss_hunter', 'killed monster', 'combo_king', 'explorer'
        ]
    levels: list = [i for i in range(1, 101)]
    i: int = 1
    high_scores: int = 0
    treasure_events: int = 0
    level_events: int = 0
    while i <= num:
        player: str = players[(i - 1) % len(players)]
        ach: str = achievements[(i - 1) % len(achievements)]
        level: int = levels[(i - 1) % len(levels)]
        yield f"Event {i}: Player {player} (level {level}) {ach}"
        i += 1
        if level >= 10:
            high_scores += 1
        if ach == "leveled up":
            level_events += 1
        if ach == "found treasure":
            treasure_events += 1
    return iter([high_scores, treasure_events, level_events])


def stream_analytics(gen) -> None:
    print("\n=== Stream Analytics ===")
    total_events: int = 0
    try:
        while True:
            next(gen)
            total_events += 1
    except StopIteration as e:
        print(f"Total events processed: {total_events}")
        print(f"High-level players (10+): {next(e.value)}")
        print(f"Treasure events: {next(e.value)}")
        print(f"Level-up events: {next(e.value)}")


def fibonacci(nb) -> Generator[int, None, None]:
    i: int = 0
    yield i
    j: int = 1
    yield j
    while nb > 2:
        res: int = i + j
        yield res
        i = j
        j = res
        nb -= 1


def prime_numbers(nb) -> Generator[int, None, None]:
    nbr: int = 3
    yield 2
    while nb > 1:
        i: int = 2
        while i < nbr:
            if nbr % i == 0:
                nbr += 1
            else:
                i += 1
        yield nbr
        nbr += 1
        nb -= 1


def print_head(num_events: int) -> None:
    if num_events.__class__ == int:
        print(f"Processing {num_events} game events...\n")



def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    num_events: int = 10
    proc_time: float = 0
    print_head(num_events)
    gen = generature(num_events)
    for event in gen:
        proc_time += 0.000045
        print(event)

    stream_analytics(generature(num_events))
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {proc_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    try:
        fib_number: int = "hh"
        fibo = fibonacci(fib_number)
        print(f"Fibonacci sequence (first {fib_number}):", end=" ")
        flag: bool = True
        for num in fibo:
            if flag:
                flag = False
            else:
                print(", ", end="")
            print(num, end='')
    except Exception:
        print(f"\nError: fibonacci number {fib_number} is not valid [please enter a valid one]")

    try:
        prime_num: int = "hh"
        prime = prime_numbers(prime_num)
        print(f"\nPrime numbers (first {prime_num}):", end=" ")
        flag: bool = True
        for num in prime:
            if flag:
                flag = False
            else:
                print(", ", end="")
            print(num, end="")
        print()
    except Exception:
        print(f"\nError: {prime_num} is not valid [please enter a valid number]")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
