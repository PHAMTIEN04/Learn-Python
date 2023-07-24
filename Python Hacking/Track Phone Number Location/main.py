# Import necessary modules
import phonenumbers
from test import number

# Import specific functions from the phonenumbers module
from phonenumbers import geocoder, carrier

# Parse the phone number using the 'number' variable from the 'test' module
parsed_number = phonenumbers.parse(number, "VN")  # Parse the phone number for Switzerland (CH)
print(geocoder.description_for_number(parsed_number, "en"))  # Print the location information for the parsed number in English

parsed_service_number = phonenumbers.parse(number, "VN")  # Parse the phone number for Romania (RO)
print(carrier.name_for_number(parsed_service_number, "en"))  # Print the carrier/service provider information for the parsed number in English
