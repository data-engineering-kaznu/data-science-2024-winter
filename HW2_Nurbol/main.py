import csv

months_mapping = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

with open('input.csv') as input_file, open('output.csv', mode='w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    header = next(csv_reader)
    csv_writer.writerow(header)

    for row in csv_reader:
        year, month_name = row[0].split('-')
        month_number = months_mapping[month_name]
        date = f"{year}-{month_number}-01"
        csv_writer.writerow([date, row[1], row[2]])
