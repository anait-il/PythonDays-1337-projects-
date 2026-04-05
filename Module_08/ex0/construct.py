import sys
import os
import site


def inside_venv() -> None:
    """Display information about the current venv"""
    print("MATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(site.getsitepackages()[0])


def outside_venv() -> None:
    """
    Demonstrate where are in the Global envirement and display information.
    """
    print("MATRIX STATUS: You're still plugged in\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


if __name__ == "__main__":
    print()
    # if sys.prefix == sys.base_prefix this mean we are in the global env.
    if sys.prefix != sys.base_prefix:
        inside_venv()
    else:
        outside_venv()
