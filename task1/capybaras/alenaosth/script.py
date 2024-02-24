import csv
new_data = []

with open('data_old.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    total =0
    for i in csv_reader:
        if total != 0 : 
            new_data.append([i[0]+'-01-01', i[1], i[2]])
            total+=1

with open('data_new.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['year', 'region', 'value'])
    for i in new_data:
        csv_writer.writerow(i)