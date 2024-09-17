import os
import requests

def get_location_data(location):
    api_key = os.getenv('GOOGLE_API_KEY')
    
    # Fetch real-time location data from Google Earth API or Google Maps API
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        raise Exception(f"Failed to retrieve data: {data.get('status')}")
    
    # Extract latitude and longitude for real-time mapping
    location_data = {
        'coordinates': data['results'][0]['geometry']['location'],
        'address': data['results'][0]['formatted_address']
    }
    
    return location_data
