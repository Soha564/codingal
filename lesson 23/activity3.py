# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

country_codes = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

print("Country code of India:", country_codes.get("India", "Not found."))
print("Country code of Japan:", country_codes.get("Japan", "Not found."))