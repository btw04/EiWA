import folium
from folium.plugins import MarkerCluster
import requests

# GBFS API endpoint
url = 'https://apis.deutschebahn.com/db-api-marketplace/apis/shared-mobility-gbfs/v2/de/CallABike/free_bike_status'

client_id = 'ec0b224441a9443450c41a514bbbb38b'
client_secret = '43d6309a2538cdca051d8986d4f21c43'

session = requests.Session()
session.headers = {
    'DB-Client-ID': client_id,
    'DB-Api-Key': client_secret
}


def get_coordinates():
    """Return a list of coordinates to pin."""
    response = session.get(url)
    data = response.json()
    coordinates = []
    for bike in data['data']['bikes']:
        coordinates.append({"lat": bike['lat'], "lon": bike['lon']})

    return coordinates


def generate_map():
    """Generate a map of Germany with pins and save it to a html file."""
    # Create a map centered around Germany
    germany_map = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

    # Create a MarkerCluster object
    marker_cluster = MarkerCluster().add_to(germany_map)

    # Get the coordinates to pin
    coordinates = get_coordinates()

    # Add pins for the coordinates
    for coord in coordinates:
        folium.Marker(location=[coord["lat"], coord["lon"]]).add_to(marker_cluster)

    # Save the map to an HTML file
    germany_map.save("germany_map.html")


generate_map()
