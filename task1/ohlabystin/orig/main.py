import csv

with open('original.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
for row in rows:
    row['year'] = row['year'] + '-01-01'
fieldnames = ['year', 'region', 'value']
with open('resulting.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        writer.writerow(row)
