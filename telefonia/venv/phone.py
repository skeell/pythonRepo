import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

numero = phonenumbers.parse('+393295636801')
print(geocoder.description_for_number(numero, 'it'))
print(carrier.name_for_number(numero,'it'))
