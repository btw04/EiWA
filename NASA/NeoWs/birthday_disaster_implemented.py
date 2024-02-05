import requests

nasa_api_key = 'RUO4ABnSnWSZ0JulyEqzIN1inFD55AxnuzOf8EBY'
url = 'https://api.nasa.gov/neo/rest/v1/feed'


def get_nearest_asteroid(day: str):
    params = {
        'start_date': day,
        'end_date': day,
        'api_key': nasa_api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    closest_asteroid = None
    closest_miss = float('inf')
    for asteroid in data['near_earth_objects'][day]:
        miss_distance = float(asteroid['close_approach_data'][0]['miss_distance']['kilometers'])
        if miss_distance < closest_miss:
            closest_miss = miss_distance
            closest_asteroid = asteroid
    return closest_asteroid


nearest = get_nearest_asteroid('2004-05-25')
print("Name: %s" % nearest['name'])
print("Miss distance: %.2f km" % float(nearest['close_approach_data'][0]['miss_distance']['kilometers']))
print("Diameter: %.2f m" % float(nearest['estimated_diameter']['meters']['estimated_diameter_max']))
