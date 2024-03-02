import csv
month = {
    'Jan': '01-01', 'Feb': '02-01', 'Mar': '03-01', 'Apr': '04-01', 'May': '05-01', 'Jun': '06-01',
    'Jul': '07-01', 'Aug': '08-01', 'Sep': '09-01', 'Oct': '10-01', 'Nov': '11-01', 'Dec': '12-01'
}
with open('gior.csv') as file:
    reader = csv.reader(file)
    data = list(reader)
for row in data:
    if '-' in row[0]:
     month_str = row[0].split('-')[1]
     row[0] = row[0].replace(month_str, month.get(month_str, ''))
with open('gior2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
