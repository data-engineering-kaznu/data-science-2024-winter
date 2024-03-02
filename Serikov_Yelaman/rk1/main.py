import csv
my_list_of_lists = []

with open('input.csv', 'r') as csv_file_for_reading:
    csv_reader = csv.reader(csv_file_for_reading)
    next(csv_reader)
    for row in csv_reader:
        pre_date = row[0]
        year = str(pre_date[0:4])
        month = str(pre_date[4:6])
        day = str(pre_date[6:8])
        post_date = month + "-" + day + "-" + year
        my_list_of_lists.append([
                                post_date, 
                                row[1],
                                row[2],
                                ])

with open('middle_output.csv', 'w', newline='') as csv_file_for_writing:
    csv_writer = csv.writer(csv_file_for_writing)
    csv_writer.writerow([
                        'year',
                        'region',
                        'value',
                        ])
    for row in my_list_of_lists:
        csv_writer.writerow(row)


my_list_of_lists_2 = []
with open('middle_output.csv', 'r') as csv_file_for_reading:
    dict_of_total_value_group_by_date = {}
    csv_reader = csv.reader(csv_file_for_reading)
    next(csv_reader)
    for row in csv_reader:
        date = row[0]
        value = int(row[2])
        if date not in dict_of_total_value_group_by_date:
            dict_of_total_value_group_by_date[date] = value
        else:
            dict_of_total_value_group_by_date[date] += value
    for key, value in dict_of_total_value_group_by_date.items():
        date = key
        total_value_group_by_date = value
        my_list_of_lists_2.append([
                                date,
                                total_value_group_by_date,
                                ])


with open('final_output.csv', 'w', newline='') as csv_file_for_writing:
    csv_writer = csv.writer(csv_file_for_writing)
    csv_writer.writerow([
                        'group_by_date',
                        'sum',
                        ])
    for row in my_list_of_lists_2:
        csv_writer.writerow(row)
