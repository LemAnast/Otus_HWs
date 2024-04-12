import requests


class BreweryApiClient:

    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1/breweries"):
        self.base_url = base_url

    def get_single_brewery(self, brewery_id):
        response = requests.get(url=f"{self.base_url}/{brewery_id}")
        return response

    def get_list_breweries_without_filters(self):
        response = requests.get(url=self.base_url)
        return response

    def get_list_breweries_by_type(self, type):
        response = requests.get(url=self.base_url, params={"by_type": type})
        return response

    def get_random_brewery(self, size):
        response = requests.get(url=f"{self.base_url}/random", params={"size": size})
        return response
