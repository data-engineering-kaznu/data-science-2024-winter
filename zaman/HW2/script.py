import csv

dates = {
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

def modify(row):
   date = row[0].split('-')[0] + '-' + dates[row[0].split('-')[1]] + '-01'
   row[0] = date
   return row

with open('input.csv') as original_csv:
  csv_reader = csv.reader(original_csv)
  next(csv_reader)
  with open('output.csv', mode='w', newline='') as result_csv:
    csv_writer = csv.writer(result_csv)
    csv_writer.writerow(['year', 'region', 'value'])
    for row in csv_reader:
        csv_writer.writerow(modify(row))