from importlib.metadata import version


def main() -> None:
    print('Checking dependencies:')
    try:
        import pandas
        import numpy
        import matplotlib.pyplot as plt

        pd = 'pandas'
        nu = 'numpy'
        mat = 'matplotlib'
        print(f'[OK] {pd} ({version(pd)}) - Data manipulation ready')
        print(f'[OK] {nu} ({version(nu)}) - Network access ready')
        print(f'[OK] {mat} ({version(mat)}) - Visualisation ready')
        print()

        print('Analyzing Matrix data...')
        n = 1000
        print(f"Processing {n} data points...")
        x = numpy.random.choice(range(n), size=10)
        y = numpy.random.choice(range(n), size=10)
        data = pandas.DataFrame({
            'x': x,
            'y': y
        })

        print("Generating Visualization...")
        plt.plot(data['x'], data['y'])
        plt.title("Analyzing Matrix Data")
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.grid(True)
        plt.savefig(('matrix_analysis.png'))
        print()
        print('Analysis complete!')
        print('Results saved to: matrix_analysis.png}')

    except ImportError:
        print("Should first install dependencies:")
        print("""
pip install -r requirements.txt # using pip
poetry install # using poetry
""")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    main()
