import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

key = 'c3e1216f2e91433c9199273e4cee8a6f'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.map(location=[])