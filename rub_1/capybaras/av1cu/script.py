import csv
import datetime

group = {}

def modify(date):
    date = datetime.datetime.strptime(date, '%Y%m%d').strftime('%d-%m-%Y')
    return date

def group_by_value(row):
    if not row[0]+row[1] in group.keys():
        group[row[0]+row[1]] = { 'date': modify(row[0]), 'region': row[1], 'value': int(row[2])}
    else:
        group[row[0]+row[1]]['value'] += int(row[2])

with open('original.csv') as original_csv:
  csv_reader = csv.reader(original_csv)
  next(csv_reader)
  with open('resulting.csv', mode='w', newline='') as result_csv:
    csv_writer = csv.writer(result_csv)
    csv_writer.writerow(['year', 'region', 'value'])
    for row in csv_reader:
        group_by_value(row)
    for g, v in group.items():
        group_value = [v['date'], v['region'], v['value']]
        csv_writer.writerow(group_value)