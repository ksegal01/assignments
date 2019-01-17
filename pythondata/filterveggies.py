#LISA S. & KATIE S.
import csv
import json
from pprint import pprint
#Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f :
	reader = csv.DictReader(f)
	vegetables = [dict(vegetable) for vegetable in reader]

# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_veggies = []
whitelist = ['okra', 'arugula', 'broccoli']
for vegetable in vegetables:
	if vegetable['name'] in whitelist:
		green_veggies.append(vegetable)


# Print veggies to the terminal
pprint(green_veggies)

# Write the veggies to a json file called greenveggies.json
with open ('greenveggies.json', 'w') as f:
	json.dump(green_veggies, f, indent=2)
with open ('green_vegetables.csv', 'w') as f:
	writer=csv.writer(f)
	writer.writerow(['name', 'color'])
	writer.writerow([green_veggies])