import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

from phone_Number import number

pepnumber = phonenumbers.parse(number)

# Get the geographical information for the phone number
location = geocoder.description_for_number(pepnumber, "en")

print(location)

# Get the carrier information for the phone number
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

# Get the exact current place of the phone number
region_data = geocoder.region_code_for_number(pepnumber)
exact_location = geocoder.description_for_number(pepnumber, "en")

print(exact_location)

# Use OpenCageGeocode to get the latitude and longitude of the location
key = '33ec4cf9b31048958ae72b7d0595bbaf'
geocoder = OpenCageGeocode(key)
query = str(exact_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

# Create a map and save it
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker(location=[lat, lng], popup=exact_location).add_to(myMap)

myMap.save("mylocation.html")
