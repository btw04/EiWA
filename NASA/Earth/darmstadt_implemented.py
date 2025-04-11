import datetime
import requests
import satellite_image_visualizer

nasa_api_key = 'RUO4ABnSnWSZ0JulyEqzIN1inFD55AxnuzOf8EBY'
url = 'https://api.nasa.gov/planetary/earth/assets'
position = (49.87731171340873, 8.656339430274041)
angel = 0.2

session = requests.Session()


def get_darmstadt_image(date: datetime):
    formatted_date = date.strftime('%Y-%m-%d')
    params = {
        'lat': position[0],
        'lon': position[1],
        'date': formatted_date,
        'dim': angel,
        'api_key': nasa_api_key
    }
    print("Requesting image for " + date.strftime('%Y-%m-%d'))
    response = session.get(url, params=params)
    print("Response: " + str(response.status_code) + "\n\n")
    data = response.json()
    if 'url' not in data:
        return None
    return data['url']


def show_darmstadt():
    date = datetime.datetime(2020, 1, 1)
    images = []
    dates = []

    # iterate through the months
    while date.year < 2023:
        image = get_darmstadt_image(date)
        if image:
            images.append(image)
            dates.append(date.strftime('%Y-%m-%d'))
        date = date + datetime.timedelta(days=30)

    print("Images: " + str(images))

    satellite_image_visualizer.display_satellite_images(images, dates)


show_darmstadt()
