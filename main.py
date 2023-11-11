import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from myphone import number  # Replace 'myphone' with the actual module or provide the phone number directly

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

service = phonenumbers.parse(number)
print(carrier.name_for_number(service, 'en'))

key = 'a3a5b051c7bf4d22915c99fa5f8251441'
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mymap)

mymap.save("mylocation.html")