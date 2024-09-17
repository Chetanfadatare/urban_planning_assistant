import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_city_layout(location_data):
    prompt = f"""
    Create a detailed city layout plan based on the following location data:
    Address: {location_data['address']}
    Coordinates: {location_data['coordinates']}
    
    Consider factors such as green spaces, zoning, population growth, and traffic management.
    Provide a comprehensive description of the suggested layout.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in urban planning."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']
