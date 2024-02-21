import csv
new_data = []

with open('data_old.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
        if i[0] != 'year':
            new_data.append([i[0]+'-01-01', i[1], i[2]])

with open('data_new.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['year', 'region', 'value'])
    for i in new_data:
        csv_writer.writerow(i)