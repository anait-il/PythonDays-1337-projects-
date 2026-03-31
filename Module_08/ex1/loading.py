from importlib.metadata import version


def main() -> None:
    print('Checking dependencies:')
    try:
        import pandas
        import numpy
        import matplotlib.pyplot as plt
        import requests

        pd = 'pandas'
        nu = 'numpy'
        mat = 'matplotlib'
        print(f'[OK] {pd} ({version(pd)}) - Data manipulation ready')
        print(f'[OK] {nu} ({version(nu)}) - Network access ready')
        print(f'[OK] {mat} ({version(mat)}) - Visualisation ready')
        print()

        print('Analyzing Matrix data...')

        url = " \
https://api.worldbank.org/v2/country/MA/indicator/NY.GDP.MKTP.CD?format=json"
        result = requests.get(url)
        data = result.json()
        record = data[1][1:10]
        years = numpy.array([item['date'] for item in record])
        values = numpy.array([item['value'] for item in record])

        n = len(years)
        print(f"Processing {n} data points...")
        year_idx = numpy.argsort(years)
        value_idx = numpy.argsort(values)
        years = years[year_idx]
        values = values[value_idx]
        data = pandas.DataFrame({
            'year': years,
            'value': values
        })

        print("Generating Visualization...")
        plt.plot(data['year'], data['value'], marker="o")
        plt.title("Analyzing Matrix Data")
        plt.xlabel('year')
        plt.ylabel('GDP (Billion USD)')
        plt.grid(True)
        plt.savefig(('matrix_analysis.png'))
        print()
        print('Analysis complete!')
        print('Results saved to: matrix_analysis.png}')

    except ImportError:
        print("Should first install dependencies:")
        print("""
pip install -r requirements.txt # using pip
poetry install --no-root # using poetry
""")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    main()
