import csv
with open("Input.csv", 'r') as input_csv, open("Output.csv", 'w') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    months = {}
    next(reader)
    writer.writerow(['year', 'region', 'value'])
    for row in reader:
        if row[1] in months:
            if row[0] in months[row[1]]:
                months[row[1]][row[0]] += int(row[2])
            else:
                months[row[1]][row[0]] = int(row[2])
        else:
            months[row[1]] = {row[0]: int(row[2])}
    for month in months:
        for date in months[month].keys():
            datep = date[4:6] + '-' + date[6:] +'-' + date[:4]
            writer.writerow([datep, month, months[month][date]])

