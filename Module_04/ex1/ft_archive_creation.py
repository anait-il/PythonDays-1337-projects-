
def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file: str = 'new_discovery.txt'
    try:
        f = None
        print("Initializing new storage unit: new_discovery.txt")
        f = open(file, 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")
        f.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f is not None:
            f.close()

    try:
        f = None
        f = open(file, 'r')
        print(f.read())
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
