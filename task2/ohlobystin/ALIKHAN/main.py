import csv

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def rename(string):
    date = str(month.index(string[0].split('-')[1]) + 1)
    if len(date) < 2:
        date = '0' + date
    return [string[0].split('-')[0]+'-'+date+'-'+'01', string[1], string[-1]]
with open('Input.csv', 'r') as input_csv, open('Output.csv', 'w') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    next(reader)
    writer.writerow(['year', 'region', 'value'])
    for row in reader:
        writer.writerow(rename(row))
