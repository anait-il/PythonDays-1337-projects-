
def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as f:
        print(f.read())

    print("\nSECURE PRESERVATION:")
    with open("classified_data.txt", "a") as f:
        data: str = "[CLASSIFIED] New security protocols archived"
        f.write(data)
        print(data)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except PermissionError as e:
        print(e)
    except FileExistsError:
        print("Error: vault not found")
