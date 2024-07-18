import requests


class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    def display_country_info(self):
        if not self.data:
            print("Data not fetched yet. Call fetch_data() first.")
            return

        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})

            if currencies:
                currency_names = ', '.join(currencies.keys())
                currency_symbols = ', '.join([info.get('symbol', 'N/A') for info in currencies.values()])
                print(f"Country: {name}")
                print(f"  Currencies: {currency_names}")
                print(f"  Currency Symbols: {currency_symbols}")
                print()

    def countries_with_dollar_currency(self):
        if not self.data:
            print("Data not fetched yet. Call fetch_data() first.")
            return

        dollar_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_code == 'USD' or currency_info.get('symbol') == '$':
                    dollar_countries.append(country.get('name', {}).get('common', 'N/A'))
                    break

        if dollar_countries:
            print("Countries with Dollar currency:")
            for country in dollar_countries:
                print(f"  - {country}")
        else:
            print("No countries found with Dollar currency.")

    def countries_with_euro_currency(self):
        if not self.data:
            print("Data not fetched yet. Call fetch_data() first.")
            return

        euro_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            if 'EUR' in currencies:
                euro_countries.append(country.get('name', {}).get('common', 'N/A'))

        if euro_countries:
            print("Countries with Euro currency:")
            for country in euro_countries:
                print(f"  - {country}")
        else:
            print("No countries found with Euro currency.")


# Example usage:
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_data = CountryData(url)

    country_data.fetch_data()

    # Display all countries with their currencies and symbols
    country_data.display_country_info()

    # Display countries with Dollar currency
    country_data.countries_with_dollar_currency()

    # Display countries with Euro currency
    country_data.countries_with_euro_currency()