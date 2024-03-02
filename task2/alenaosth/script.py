import csv

month_dict = {
    "Jan": "01-01",
    "Feb": "02-01",
    "Mar": "03-01",
    "Apr": "04-01",
    "May": "05-01",
    "Jun": "06-01",
    "Jul": "07-01",
    "Aug": "08-01",
    "Sep": "09-01",
    "Oct": "10-01",
    "Nov": "11-01",
    "Dec": "12-01"
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



