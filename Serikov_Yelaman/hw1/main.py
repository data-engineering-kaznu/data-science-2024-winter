import csv
my_list_of_lists = []

with open('input.csv', 'r') as csv_file_for_reading:
    csv_reader = csv.reader(csv_file_for_reading)
    next(csv_reader)
    for row in csv_reader:
        my_list_of_lists.append([
                                row[0]+'-01-01', 
                                row[1],
                                row[2],
                                ])

with open('output.csv', 'w', newline='') as csv_file_for_writing:
    csv_writer = csv.writer(csv_file_for_writing)
    csv_writer.writerow([
                        'year',
                        'region',
                        'value',
                        ])
    for row in my_list_of_lists:
        csv_writer.writerow(row)
