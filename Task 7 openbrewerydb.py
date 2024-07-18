import requests


def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


states = ['Alaska', 'Maine', 'New York']

for state in states:
    breweries = fetch_breweries_by_state(state)
    if breweries:
        print(f"Breweries in {state}:")
        for brewery in breweries:
            print(brewery['name'])
        print()
    else:
        print(f"Failed to fetch data for {state}")
for state in states:
    breweries = fetch_breweries_by_state(state)
    if breweries:
        print(f"Number of breweries in {state}: {len(breweries)}")
    else:
        print(f"Failed to fetch data for {state}")


def count_brewery_types_by_city(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        city_breweries = {}
        for brewery in breweries:
            city = brewery['city']
            brewery_type = brewery['brewery_type']
            if city not in city_breweries:
                city_breweries[city] = set()
            city_breweries[city].add(brewery_type)
        city_types_count = {city: len(types) for city, types in city_breweries.items()}
        return city_types_count
    else:
        return None


for state in states:
    city_types_count = count_brewery_types_by_city(state)
    if city_types_count:
        print(f"City-wise brewery type counts in {state}:")
        for city, count in city_types_count.items():
            print(f"{city}: {count}")
        print()
    else:
        print(f"Failed to fetch data for {state}")


def count_breweries_with_websites(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        count_with_website = sum(1 for brewery in breweries if brewery['website_url'] is not None)
        return count_with_website
    else:
        return None


for state in states:
    count_with_website = count_breweries_with_websites(state)
    if count_with_website is not None:
        print(f"Number of breweries with websites in {state}: {count_with_website}")
    else:
        print(f"Failed to fetch data for {state}")
