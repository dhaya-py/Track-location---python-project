import phonenumbers
from myphone import number
import opencage
import folium

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(f"Location of the given number : {location}")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(f"Service name : {carrier.name_for_number(service_pro, 'en')}")

from opencage.geocoder import OpenCageGeocode

key = "7ed56386de784f14be1dcb6860276009"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"lat : {lat}, lng : {lng}")

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")