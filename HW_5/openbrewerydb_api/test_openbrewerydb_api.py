import pytest

from HW_5.openbrewerydb_api.openbrewerydb_api_client import BreweryApiClient
from pydantic import BaseModel
from typing import Optional

brewery = BreweryApiClient()


class BreweryModel(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: str
    street: Optional[str] = None


@pytest.mark.parametrize("brewery_id", ["42aa37d5-8384-4ffe-8c81-7c982eff0384",
                                        "4f4b5b34-d572-4dff-a18f-47e507c073e6",
                                        "5128df48-79fc-4f0f-8b52-d06be54d0cec"])
def test_get_single_brewery(brewery_id):
    response = brewery.get_single_brewery(brewery_id)
    response_json = response.json()
    assert response.status_code == 200
    assert BreweryModel.parse_obj(response_json)
    assert response_json["id"] == brewery_id


def test_get_single_brewery_negative(brewery_id="1"):
    response = brewery.get_single_brewery(brewery_id)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["message"] == "Couldn't find Brewery"


def test_get_list_breweries_without_filters():
    response = brewery.get_list_breweries_without_filters()
    response_json = response.json()
    breweries = [BreweryModel.parse_obj(obj) for obj in response_json]
    assert response.status_code == 200
    assert len(breweries) == 50


@pytest.mark.parametrize("type", ["micro", "nano", "regional", "brewpub",
                                  "large", "planning", "bar", "contract",
                                  "proprietor", "closed"])
def test_get_list_breweries_by_type(type):
    response = brewery.get_list_breweries_by_type(type)
    response_json = response.json()
    breweries = [BreweryModel.parse_obj(obj) for obj in response_json]
    assert response.status_code == 200
    for obj in breweries:
        assert obj.brewery_type == type


@pytest.mark.parametrize("size", [1, 3, 5, 10])
def test_get_random_brewery(size):
    response = brewery.get_random_brewery(size)
    response_json = response.json()
    breweries = [BreweryModel.parse_obj(obj) for obj in response_json]
    assert len(breweries) == size
    assert response.status_code == 200

