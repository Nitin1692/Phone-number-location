import phonenumbers
from myphone import number

from phonenumbers import geocoder
from phonenumbers import carrier

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))