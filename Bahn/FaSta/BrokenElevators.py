import requests

# FaSta API endpoint
facilities_url = 'https://apis.deutschebahn.com/db-api-marketplace/apis/fasta/v2/facilities'

# include these in the header of the request as 'DB-Client-ID' and 'DB-Api-Key'
client_id = 'ec0b224441a9443450c41a514bbbb38b'
client_secret = '43d6309a2538cdca051d8986d4f21c43'

session = requests.Session()
session.headers = {
    # TODO: Add the headers to the session
}

"""
Example of how to set parameters for a request:
params = {'active': False, 'allow': [0, 1, 5]}
"""


def get_working():
    """Return a list of working elevators."""
    params = {
        # TODO: Add the parameters to the request
    }
    response = session.get(facilities_url, params=params)
    data = response.json()
    return len(data)


def get_broken():
    """Return a list of broken/unknown elevators."""
    params = {
        # TODO: Add the parameters to the request
    }
    response = session.get(facilities_url, params=params)
    data = response.json()
    return len(data)


working = get_working()
broken = get_broken()
print("%d out of %d elevators are broken. (%.2f %%)" % (broken, working + broken, broken / (working + broken) * 100))
