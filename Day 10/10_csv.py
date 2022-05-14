import csv

# with open('info.csv', 'r') as f:
# 	for line in f:
# 		print(line[0:5])

# with open('info.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)

# 	next(csv_reader)

# 	for i in csv_reader:
# 		print(i[0])


with open('info.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_info.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t')

		for line in csv_reader:
			csv_writer.writerow(line)
