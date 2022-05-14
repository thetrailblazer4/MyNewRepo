import csv

with open('info.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('dict_info.csv', 'w') as new_file:
		fieldnames = ['first_name', 'email']

		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,delimiter='\t')
		csv_writer.writeheader()
		for line in csv_reader:
			del line['last_name']
			csv_writer.writerow(line)
