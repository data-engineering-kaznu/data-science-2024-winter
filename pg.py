import csv

with open("Input.csv", 'r') as input_csv, open("Output.csv", 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    months = {}

    header = next(reader)
    writer.writerow(['year', 'region', 'value'])

    for row in reader:
        year = row[0][:4]
        month = row[0][4:6]
        day = row[0][6:]
        date_formatted = f"{day}-{month}-{year}"

        region = row[1]
        value = int(row[2])

        if region in months:
            if date_formatted in months[region]:
                months[region][date_formatted] += value
            else:
                months[region][date_formatted] = value
        else:
            months[region] = {date_formatted: value}

    for region, dates in months.items():
        for date, value in dates.items():
            writer.writerow([date, region, value])

