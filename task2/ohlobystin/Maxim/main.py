import csv

months = {
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
   'Dec': '12'
}

with open('Input.csv', 'r') as input_csv, open('Output.csv', 'w') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    next(reader)
    writer.writerow(['year', 'region', 'value'])
    for row in reader:
        row[0] = row[0].split('-')[0] + '-' + months[row[0].split('-')[1]] +'-'+'01'
        writer.writerow(row)
