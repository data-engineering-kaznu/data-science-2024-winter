import csv

with open("Input.csv", 'r', newline='') as r_file, open('Output.csv', 'w', newline='') as w_file:
    reader = csv.reader(r_file)
    writer = csv.writer(w_file)
    writer.writerow(['year', 'region', 'value'])  # Write header
    for row in reader:
        year, region, value = row
        year = year + '-01-01'  # Assuming year is in YYYY format
        writer.writerow([year, region, value])

