
def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    f = None
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        f = open('ancient_fragment.txt')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception:
        print("ERROR: Storage vault not found.")
        print("Run data generator first.")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
