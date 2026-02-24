
def crisis_handler(file: str) -> None:
    try:

        with open(file) as f:
            data: str = f.read()

        print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(e)


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files: list = ["lost_archive.txt",
                   "classified_vault.txt",
                   "standard_archive.txt"]
    for file in files:
        crisis_handler(file)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
