#Write the vegetable to a CSV file
import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "cauliflower", "color": "white"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	#write header
	writer.writerow(['name', 'color', 'length_of_name'])
	#write data

	# Loop through each vegetable
	for vegetable in vegetables:
		name = vegetable['name']
		color = vegetable['color']
		length_of_name = len(vegetable['name'])
		writer.writerow([name,color, length_of_name])