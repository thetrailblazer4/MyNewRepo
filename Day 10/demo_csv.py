# import csv

# with open('new_info.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter='\t')

# 	for line in csv_reader:
# 		print(line)


import csv

with open('info.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for line in csv_reader:
		print(line['email'])
