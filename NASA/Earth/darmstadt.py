import datetime
import requests
import satellite_image_visualizer


# Parameters
nasa_api_key = 'RUO4ABnSnWSZ0JulyEqzIN1inFD55AxnuzOf8EBY'
url = 'https://api.nasa.gov/planetary/earth/assets'
position = (49.87731171340873, 8.656339430274041)
angel = 0.2

# HTTP Session
session = requests.Session()


def get_darmstadt_image(date: datetime):
    """
    Get the satellite image of Darmstadt for a specific date
    """
    formatted_date = date.strftime('%Y-%m-%d')
    params = {
        # TODO: Add parameters for the request (lat, lon, date, dim, api_key)
    }
    print("Requesting image for " + date.strftime('%Y-%m-%d'))
    response = session.get(url, params=params)
    print("Response: " + str(response.status_code) + "\n\n")
    data = response.json()

    # TODO: Return the URL of the image from the response
    return "https://earthengine.googleapis.com/:getPixels"


def show_darmstadt():
    """
    Show satellite images of Darmstadt over time
    """
    date = datetime.datetime(2020, 1, 1)
    images = []
    dates = []

    # iterate through the months. 2023 is the hard limit as there are no images available after 2022.
    while date.year < 2023:
        image = get_darmstadt_image(date)
        if image:
            images.append(image)
            dates.append(date.strftime('%Y-%m-%d'))
        date = date + datetime.timedelta(days=30)

    print("Images: " + str(images))

    # Display the images using the SatelliteImageVisualizer. Note that this causes a mass-download of images.
    satellite_image_visualizer.display_satellite_images(images, dates)


show_darmstadt()
