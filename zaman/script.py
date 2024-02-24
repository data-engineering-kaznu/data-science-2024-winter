import csv

with open('input.csv', 'r') as csv_file, open('output.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_file)

    # Write the header to the output file
    csv_writer.writerow(['year', 'region', 'value'])

    # Read each row from the input file
    for row in csv_reader:
        # Skip the header row
        if row[0] == 'year':
            continue

        # Convert the year to a date in the format 'YYYY-MM-DD'
        date = row[0] + '-01-01'

        # Write the modified row to the output file
        csv_writer.writerow([date, row[1], row[2]])