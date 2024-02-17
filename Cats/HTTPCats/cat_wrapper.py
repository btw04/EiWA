import requests
from PIL import Image
from io import BytesIO

session = requests.Session()
cat_url = 'https://http.cat/'


def get(url, params=None):
    response = session.get(url, params=params)
    display_status_cat(response.status_code)
    return response


def post(url, data=None):
    response = session.post(url, data=data)
    display_status_cat(response.status_code)
    return response


def display_status_cat(code):
    # TODO: Implement the request to the cat API
    response = None
    image = Image.open(BytesIO(response.content))
    image.show()
