import pytest

from HW_5.jsonplaceholder_api.jsonplaceholder_api_client import JsonApiClient
from pydantic import BaseModel


client = JsonApiClient()


class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str


@pytest.mark.parametrize("post_id", [1, 25, 50, 100])
def test_get_post_by_id(post_id):
    response = client.get_post_by_id(post_id)
    response_json = response.json()
    assert response.status_code == 200
    post = PostModel.model_validate(response_json)
    assert post.id == post_id


def test_get_post_by_id_negative(post_id=0):
    response = client.get_post_by_id(post_id)
    assert response.status_code == 404


def test_get_all_posts():
    response = client.get_all_posts()
    response_json = response.json()
    assert response.status_code == 200
    assert [PostModel.parse_obj(obj) for obj in response_json]


@pytest.mark.parametrize("title, body, user_id",
                         [("Test title", "Test body", 5),
                          ("", "", 1),
                          ("05456", "68716", 10)])
def test_create_post(title, body, user_id):
    response = client.create_post(title, body, user_id)
    response_json = response.json()
    assert response.status_code == 201
    post = PostModel.model_validate(response_json)
    assert post.title == title
    assert post.body == body
    assert post.userId == user_id


@pytest.mark.parametrize("post_id, title, body, user_id",
                         [(1, "Test title", "Test body", 1),
                          (2, "", "", 1),
                          (10, "05456", "68716", 10)])
def test_update_post(post_id, title, body, user_id):
    response = client.update_post(post_id, title, body, user_id)
    response_json = response.json()
    assert response.status_code == 200
    post = PostModel.model_validate(response_json)
    assert post.id == post_id
    assert post.title == title
    assert post.body == body
    assert post.userId == user_id


@pytest.mark.parametrize("post_id", [1, 10, 25])
def test_delete_post(post_id):
    response = client.delete_post(post_id)
    response_json = response.json()
    assert response.status_code == 200
    assert not response_json
