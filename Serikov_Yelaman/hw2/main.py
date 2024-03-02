import csv

my_months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}

my_list_of_lists = []

with open('input.csv', 'r') as csv_file_for_reading:
    csv_reader = csv.reader(csv_file_for_reading)
    next(csv_reader)
    for row in csv_reader:
        year_and_month = row[0].split('-')
        year = year_and_month[0]
        month = year_and_month[1]
        month = my_months[month]
        my_list_of_lists.append([
                                year + '-' + month + '-01', 
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
