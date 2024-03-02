import csv

with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    csv_writer.writerow(next(csv_reader))

    for row in csv_reader:
        row[0] = row[0][4:6] + '-' + row[0][6:] + '-' + row[0][:4]
        row[2] = str(int(row[2]) + int(next(csv_reader)[2]))
        csv_writer.writerow(row)
