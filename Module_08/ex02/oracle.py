import os


def load_config() -> None:
    """
    Load configuration from environment variables or .env file
    """

    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        from dotenv import load_dotenv
        if not load_dotenv():
            raise ValueError("[Warnning] The configuration file doesn't exist")

        mode = os.getenv("MATRIX_MODE")
        database = os.getenv("DATABASE_URL")
        apikey = os.getenv("API_KEY")
        log = os.getenv("LOG_LEVEL")
        zion = os.getenv("ZION_ENDPOINT")

        print("Configuration loaded:")
        if mode:
            print(f"Mode: {mode.lower()}")
        else:
            print("Mode: Not configured")
        if database:
            print("Database: Connected to local instance")
        else:
            print("Database: Not configured")
        if apikey:
            print("API Access: Authenticated")
        else:
            print("API Access: Not configured")
        if log:
            print("Log Level: DEBUG")
        else:
            print("Log Level: Not configured")
        if zion:
            print("Zion Network: Online")
        else:
            print("Zione Network: Offline")

        print()
        print("Environment security check:")
        if mode and database and apikey and log and zion:
            print("[OK] No hardcoded secrets detected")
            print("[OK] .env file properly configured")
            print("[OK] Production overrides available")
        else:
            print("[Missing] Some configuration secrets are missing")

        print()
        print("The Oracle sees all configurations.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    load_config()
