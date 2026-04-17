"""
DEPRECATED, needs to migrate to NASA-GIBS


import datetime
import requests
import math
import satellite_image_visualizer

# No API Key required for standard GIBS WMTS requests
BASE_URL = "https://gibs.earthdata.nasa.gov/wmts/epsg4326/best"
LAYER = "VIIRS_SNPP_CorrectedReflectance_TrueColor"
POSITION = (49.87731171340873, 8.656339430274041)
ZOOM_LEVEL = 9  # TileMatrix

session = requests.Session()


def get_tile_coords(lat, lon, z):
    # At Zoom level Z, there are 2^(Z) tiles vertically (180 deg)
    # and 2^(Z+1) tiles horizontally (360 deg).
    num_tiles_y = 2 ** z
    num_tiles_x = 2 ** (z + 1)

    # Map lat [-90, 90] and lon [-180, 180] to tile indices
    x = int((lon + 180) / 360 * num_tiles_x)
    y = int((90 - lat) / 180 * num_tiles_y)

    return x, y


def get_darmstadt_gibs_url(date: datetime):
    formatted_date = date.strftime('%Y-%m-%d')
    x, y = get_tile_coords(POSITION[0], POSITION[1], ZOOM_LEVEL)

    # Construct the Direct URL
    # format: .../{Layer}/default/{Date}/{TileMatrixSet}/{Z}/{Y}/{X}.jpg
    tile_url = f"{BASE_URL}/{LAYER}/default/{formatted_date}/250m/{ZOOM_LEVEL}/{y}/{x}.jpg"

    # Check if tile exists for that date
    print(f"Checking GIBS for {formatted_date}...")
    response = session.head(tile_url)  # HEAD request is faster to check existence

    if response.status_code == 200:
        return tile_url
    else:
        print(f"No image found for {formatted_date} (Status: {response.status_code})")
        return None


def show_darmstadt():
    date = datetime.datetime(2020, 1, 1)
    images = []
    dates = []

    while date.year < 2023:
        image_url = get_darmstadt_gibs_url(date)
        if image_url:
            images.append(image_url)
            dates.append(date.strftime('%Y-%m-%d'))

        # Advance 30 days
        date = date + datetime.timedelta(days=30)

    if images:
        print(f"Found {len(images)} images.")
        satellite_image_visualizer.display_satellite_images(images, dates)
    else:
        print("No images found in the specified range.")


if __name__ == "__main__":
    show_darmstadt()
"""