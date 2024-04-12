import requests


class JsonApiClient:

    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_post_by_id(self, post_id):
        response = requests.get(url=f"{self.base_url}/posts/{post_id}")
        return response

    def get_all_posts(self):
        response = requests.get(url=f"{self.base_url}/posts")
        return response

    def create_post(self, title, body, user_id):
        response = requests.post(url=f"{self.base_url}/posts",
                                 json={"title": title, "body": body, "userId": user_id})
        return response

    def update_post(self, post_id, title, body, user_id):
        response = requests.put(url=f"{self.base_url}/posts/{post_id}",
                                json={"id": post_id, "title": title, "body": body, "userId": user_id})
        return response

    def delete_post(self, post_id):
        response = requests.delete(url=f"{self.base_url}/posts/{post_id}")
        return response
