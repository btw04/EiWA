import requests

# FaSta API endpoint
facilities_url = 'https://apis.deutschebahn.com/db-api-marketplace/apis/fasta/v2/facilities'

# include these in the header of the request as 'DB-Client-ID' and 'DB-Api-Key'!
client_id = 'ec0b224441a9443450c41a514bbbb38b'
client_secret = '43d6309a2538cdca051d8986d4f21c43'

session = requests.Session()
session.headers = {
    'DB-Client-ID': client_id,
    'DB-Api-Key': client_secret
}


def get_working():
    """Return a list of working elevators."""
    params = {'type': 'ELEVATOR', 'state': 'ACTIVE'}
    response = session.get(facilities_url, params=params)
    data = response.json()
    return len(data)


def get_broken():
    """Return a list of broken/unknown elevators."""
    params = {'type': 'ELEVATOR', 'state': 'INACTIVE,UNKNOWN'}
    response = session.get(facilities_url, params=params)
    data = response.json()
    return len(data)


def get_equipment_numbers():
    """Return a list of equipment-numbers of broken/unknown elevators."""
    response = session.get(facilities_url, params={'type': 'ELEVATOR', 'state': 'INACTIVE,UNKNOWN'})
    data = response.json()
    return len(data)


def get_broken_elevators_data(equip_numbers):
    """Return a list of dictionaries with broken elevators data."""
    broken_elevators = []
    for equip_number in equip_numbers:
        response = session.get(facilities_url + '/' + str(equip_number))
        data = response.json()
        broken_elevators.append(data)

    return broken_elevators


print("%d out of %d elevators are broken. (%.2f %%)" % (get_broken(), get_working() + get_broken(), get_broken() / (get_working() + get_broken()) * 100))
