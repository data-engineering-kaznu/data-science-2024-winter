import csv
data=[]
with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == '0':
            data.append(row)
        else:
            data.append([row[0] + '-01-01', row[1], row[2]])

with open('test2.csv', mode='w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=',')
    for i in data:
        csv_writer.writerow(i)