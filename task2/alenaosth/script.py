import csv
from datetime import datetime

dict = {
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

next(csv_reader)

for row in csv_reader:

    month_name = row[0].split('-')[1]

    month_num = dict.get(month_name)

    if month_num:
        row[0] = row[0].replace(month_name, month_num)

csv_writer.writerow(row)
