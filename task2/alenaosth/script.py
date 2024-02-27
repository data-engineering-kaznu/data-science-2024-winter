import csv

month_dict = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}

with open('data_old2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('data_new2.csv', 'w', newline='') as csv_file_new:
        csv_writer = csv.writer(csv_file_new)

        headers = next(csv_reader)
        csv_writer.writerow(headers)

        for row in csv_reader:
            month_name = row[0].split('-')[1]
            month_num = month_dict.get(month_name)

            if month_num:
                row[0] = row[0].replace(month_name, month_num)

            csv_writer.writerow(row)

        csv_file_new.write('\n')



modified_data = []

with open('data_old2.csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
        if i[0] != 'year':
            modified_data.append([i[0]+'-01-01', i[1], i[2]])

with open('data_new2.csv.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for i in modified_data:
        csv_writer.writerow(i)