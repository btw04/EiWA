import requests

nasa_api_key = 'RUO4ABnSnWSZ0JulyEqzIN1inFD55AxnuzOf8EBY'
url = 'https://api.nasa.gov/neo/rest/v1/feed'


def get_nearest_asteroid(day: str):
    params = {
        # TODO add parameters (start_date, end_date, api_key) to the request
    }
    response = requests.get(url, params=params)
    data = response.json()
    closest_asteroid = None
    closest_miss = float('inf')
    # TODO return the closest asteroid
    return closest_asteroid


nearest = get_nearest_asteroid('2004-05-25')
print("Name: %s" % nearest['name'])
print("Miss distance: %.2f km" % float(nearest['close_approach_data'][0]['miss_distance']['kilometers']))
print("Diameter: %.2f m" % float(nearest['estimated_diameter']['meters']['estimated_diameter_max']))
