
def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file: str = 'new_discovery.txt'
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open(file, 'w') as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            f.write("[ENTRY 001] New quantum algorithm discovered\n")
            f.write("[ENTRY 002] Efficiency increased by 347%\n")
            f.write("[ENTRY 003] Archived by Data Archivist trainee\n")

        with open(file, 'r') as f:
            print(f.read())
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
