import phonenumbers

import folium

from phonetracker import number

from phonenumbers import parse

from phonenumbers import carrier,geocoder

from opencage.geocoder import OpenCageGeocode

# OpenCage API key
api_key = '2b10a3d681e245d8b877089c0f8df588'

# Phone number to lookup

#parse phone number
moriNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(moriNumber, "en")

#get phone number's carrier
service_provider = phonenumbers.parse(number)
print("Carrier : ",carrier.name_for_number(service_provider,"en"))

# get the location using opencage geocoding API
geocoder = OpenCageGeocode(api_key)
result = geocoder.geocode(str(yourlocation))

print(result)

# Extract the coordinates
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(f'Exact location of phone number: {lat},{lng}')

# Create the map
myMap = folium.Map(location=[lat, lng], zoom_start = 9)

# Add a marker to the map
folium.Marker([lat, lng],popup=service_provider).add_to(myMap)

# Save the map to an HTML file
myMap.save("myLocation.html")
