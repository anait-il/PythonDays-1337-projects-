
def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file: str = 'new_discovery.txt'
    data: str = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee
"""
    f = False
    try:
        print(f"Initializing new storage unit: {file}")
        f = open(file, 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write(data)
        print(data)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    main()

