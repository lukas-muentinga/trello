from requests import Session
from requests_oauthlib import OAuth1

from . import config

url = 'https://api.trello.com/1/'


class Trello (Session):
    """TODO: Docstring"""

    def __init__(self):
        super().__init__()
        self.auth = OAuth1(client_key=config.APP_KEY, resource_owner_key=config.API_TOKEN)

    def get(self, path, json=None, data=None):
        # TODO: doku
        return super().get(f'{url}/{path}', json=json, data=data)

    def post(self, path, data=None, json=None):
        # TODO: doku
        return super().post(f'{url}/{path}', data=data, json=json)

    def patch(self, url, data=None, json=None):
        # TODO: implement
        super().patch(url, data=data, json=json)

    def delete(self, url):
        # TODO: implement
        super().delete(url)