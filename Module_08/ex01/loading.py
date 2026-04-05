from importlib.metadata import version


def main() -> None:
    """
    Get the json data from url and use it to make a plot.
    """
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
        years = years[year_idx]
        values = values[year_idx]
        data = pandas.DataFrame({
            'year': years,
            'value': values
        })

        figure = 'matrix_analysis.png'
        print("Generating Visualization...")
        plt.plot(data['year'], data['value'], marker="o")
        plt.title("Analyzing Matrix Data")
        plt.xlabel('year')
        plt.ylabel('GDP (Billion USD)')
        plt.grid(True)
        plt.savefig((figure))

        print()
        print('Analysis complete!')
        print(f'Results saved to: {figure}')

    except ImportError:
        print("Should first install dependencies:")
        print("""
pip install -r requirements.txt # using pip
(you should run this in venv to avoid conflict)

poetry install --no-root # using poetry
poetry run python loading.py
""")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    main()
