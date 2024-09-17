import os
from dotenv import load_dotenv
from gis_utils import get_location_data
from ai_utils import generate_city_layout
import pydeck as pdk
import streamlit as st

load_dotenv()

# Real-time user input and dynamic map update
def main():
    st.title("AI-Driven Urban Planning Assistant")

    # Take user input for location
    location = st.text_input("Enter village name in India:", "example_village")

    if location:
        try:
            # Fetch real-time location data from Google Earth API
            location_data = get_location_data(location)

            # Display the location data
            st.write(f"Location Data for {location}:")
            st.write(location_data)

            # Generate a real-time city layout based on location data
            city_layout = generate_city_layout(location_data)

            # Display the city layout suggestion (from OpenAI)
            st.write("AI-Generated City Layout Suggestion:")
            st.write(city_layout)

            # Render the real-time 3D map
            render_3d_map(location_data)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Render the 3D map using Pydeck
def render_3d_map(location_data):
    lat = location_data['coordinates']['lat']
    lon = location_data['coordinates']['lng']
    
    # Define the initial view state for 3D visualization
    view_state = pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=15,
        pitch=50  # Adjust for a 3D effect
    )
    
    # Create a 3D Hexagon layer representing buildings or areas
    layer = pdk.Layer(
        'HexagonLayer',  # For demo purposes; can be replaced with other layers
        data=[],  # You can fill this with real data
        get_position='[longitude, latitude]',
        elevation_scale=50,
        radius=200,
        extruded=True,
        pickable=True
    )
    
    # Render the map with real-time updates
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "City Layout"})
    st.pydeck_chart(r)

if __name__ == "__main__":
    main()
